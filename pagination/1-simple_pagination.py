#!/usr/bin/env python3
"""
Module for simple pagination of a dataset.
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return start and end index for a given pagination page and page size.

    Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

    Returns:
        Tuple[int, int]: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with no cached dataset."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # remove header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): Page number (must be > 0)
            page_size (int): Number of items per page (must be > 0)

        Returns:
            List[List]: The requested page of data, or empty list if out of range
        """
        assert isinstance(page, int) and page > 0, "page must be an integer > 0"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be an integer > 0"

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        if start >= len(dataset):
            return []

        return dataset[start:end]
