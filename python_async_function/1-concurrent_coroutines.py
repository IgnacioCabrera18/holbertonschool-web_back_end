#!/usr/bin/env python3
"""
Asynchronous utilities module.

This module provides functions to run multiple wait_random coroutines
concurrently and collect their results in completion order.
"""

from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    a list of all delays in ascending order without using sort().

    :param n: Number of times to call wait_random.
    :param max_delay: Maximum number of seconds for each wait.
    :return: List of floats representing all delays in completion order.

    Examples:
    >>> import asyncio
    >>> asyncio.run(wait_n(5, 5))  # returns list of 5 floats
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
