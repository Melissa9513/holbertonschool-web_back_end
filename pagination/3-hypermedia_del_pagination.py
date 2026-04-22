#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict:
        """
        Return a page of data with deletion-resilient pagination.

        Args:
            index (int): Starting index
            page_size (int): Number of items per page

        Returns:
            Dict: Pagination data
        """
        dataset = self.indexed_dataset()

        assert isinstance(index, int) and index >= 0
        assert index < len(dataset)

        data = []
        current_index = index
        collected = 0

        # collect page_size items, skipping missing indexes
        while collected < page_size and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
                collected += 1
            current_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index
        }
