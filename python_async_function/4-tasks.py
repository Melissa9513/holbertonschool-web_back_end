#!/usr/bin/env python3
"""
Module that runs multiple asyncio tasks concurrently.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times and returns the list of delays
    in ascending order.

    Args:
        n (int): number of tasks to spawn
        max_delay (int): maximum delay value

    Returns:
        List[float]: list of delays sorted in ascending order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
