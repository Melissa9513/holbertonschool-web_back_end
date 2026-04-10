#!/usr/bin/env python3
"""
Module that runs multiple coroutines concurrently using asyncio.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times and returns the list of delays
    in ascending order.

    Args:
        n (int): number of times to call wait_random
        max_delay (int): maximum delay value

    Returns:
        List[float]: list of delays sorted in ascending order
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        results.append(delay)

    return results
