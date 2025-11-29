#!/usr/bin/env python3
"""
Asynchronous utilities module.

This module provides basic asynchronous functions using asyncio.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return it.

    :param max_delay: Maximum number of seconds to wait (default 10).
    :return: The actual number of seconds waited as a float.

    Examples:
    >>> import asyncio
    >>> asyncio.run(wait_random(2))  # returns a float <= 2
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
