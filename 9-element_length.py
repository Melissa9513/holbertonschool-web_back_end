#!/usr/bin/env python3
"""
Module that provides a function returning elements with their lengths.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element
    and its length.

    Args:
        lst (Iterable[Sequence]): iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: list of (element, length)
    """
    return [(i, len(i)) for i in lst]
