#!/usr/bin/env python3
"""
Module that provides a function returning a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): value used to multiply inputs

    Returns:
        Callable[[float], float]: function that multiplies a float by multiplier
    """
    def multiply(x: float) -> float:
        return x * multiplier

    return multiply
