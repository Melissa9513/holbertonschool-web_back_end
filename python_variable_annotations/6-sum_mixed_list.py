#!/usr/bin/env python3
"""
Module that provides a function to sum a list of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): list of numbers (int or float)

    Returns:
        float: sum of all elements in mxd_lst
    """
    return float(sum(mxd_lst))
