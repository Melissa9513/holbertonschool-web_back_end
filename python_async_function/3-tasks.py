#!/usr/bin/env python3
"""
Module that creates an asyncio Task from a coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that schedules wait_random.

    Args:
        max_delay (int): maximum delay value

    Returns:
        asyncio.Task: a scheduled task running wait_random(max_delay)
    """
    return asyncio.create_task(wait_random(max_delay))
