#!/usr/bin/env python3
"""
Function utilities module.

This module provides higher-order functions such as multipliers.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.

    :param multiplier: A float to multiply by.
    :return: A function that takes a float and returns it multiplied.

    Examples:
    >>> doubler = make_multiplier(2.0)
    >>> doubler(3.0)
    6.0
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
