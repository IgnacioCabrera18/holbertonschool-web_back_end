#!/usr/bin/env python3
"""
Conversion utilities module.

This module provides simple functions for basic type conversions.
It currently includes the 'to_str' function for converting floats to strings.
"""


def to_str(n: float) -> str:
    """
    Convert a floating-point number to a string.

    :param n: The input float.
    :return: The string representation of 'n'.

    Examples:
    >>> to_str(3.14)
    '3.14'
    >>> to_str(0.0)
    '0.0'
    >>> to_str(-2.5)
    '-2.5'
    """
    return str(n)
