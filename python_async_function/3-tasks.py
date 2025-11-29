#!/usr/bin/env python3
"""
Task creation module.

This module provides a function to create asyncio tasks from
the wait_random coroutine.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine with max_delay.

    :param max_delay: Maximum number of seconds for wait_random.
    :return: An asyncio.Task object.

    Example:
    >>> import asyncio
    >>> task = task_wait_random(5)
    >>> isinstance(task, asyncio.Task)
    True
    """
    return asyncio.create_task(wait_random(max_delay))
