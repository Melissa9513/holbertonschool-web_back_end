#!/usr/bin/env python3
"""
Module that provides a coroutine using async comprehension.
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using
    an async comprehension.

    Returns:
        List[float]: list of 10 random numbers
    """
    return [i async for i in async_generator()]
