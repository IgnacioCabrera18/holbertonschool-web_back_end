#!/usr/bin/env python3
"""
Concurrent tasks module.

This module provides a function to create multiple asyncio tasks using
task_wait_random and collect their results in completion order.
"""

from typing import List
import asyncio

# Import task_wait_random from 3-tasks.py
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and return
    a list of all delays in completion order.

    :param n: Number of times to call task_wait_random.
    :param max_delay: Maximum number of seconds for each wait.
    :return: List of floats representing all delays in completion order.

    Examples:
    >>> import asyncio
    >>> asyncio.run(task_wait_n(5, 5))  # returns list of 5 floats
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)
    return delays
