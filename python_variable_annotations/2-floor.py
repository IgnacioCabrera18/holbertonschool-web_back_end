#!/usr/bin/env python3
"""
Math utilities module.

This module includes simple math functions, such as 'floor'.
"""

import math


def floor(n: float) -> int:
    """
    Return the floor of a floating-point number.

    :param n: The input float number.
    :return: The floor of 'n' as an integer.

    Examples:
    >>> floor(3.14)
    3
    >>> floor(-2.7)
    -3
    >>> floor(5.0)
    5
    """
    return math.floor(n)
