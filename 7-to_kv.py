#!/usr/bin/env python3
"""
Module that provides a function to return a tuple with a string and
the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing a string and the square of a number.

    Args:
        k (str): the key string
        v (Union[int, float]): number to square

    Returns:
        Tuple[str, float]: (k, v squared as float)
    """
    return (k, float(v ** 2))
