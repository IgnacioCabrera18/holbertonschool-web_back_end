#!/usr/bin/env python3
"""
Runtime measurement module.

This module provides a function to measure the average runtime of
the wait_n coroutine from 1-concurrent_coroutines.py.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).

    :param n: Number of times to call wait_random inside wait_n.
    :param max_delay: Maximum number of seconds for each wait.
    :return: Average runtime per coroutine in seconds as a float.

    Examples:
    >>> measure_time(5, 5)  # returns a float
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time: float = end - start
    return total_time / n
