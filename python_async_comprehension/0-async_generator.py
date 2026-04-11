#!/usr/bin/env python3
"""
Module that provides an asynchronous generator yielding random numbers.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random numbers between 0 and 10.

    Yields:
        float: a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
