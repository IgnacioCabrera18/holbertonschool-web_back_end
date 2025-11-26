#!/usr/bin/env python3
"""
Mathematical Utilities Module.

This module provides simple functions for performing basic mathematical operations.
Currently, it only contains the 'add' function for addition.
"""

def add(a: float, b: float) -> float:
    """
    Sums two floating-point numbers.

    Takes two numbers (floats or integers) and returns their sum.

    :param a: The first number (float).
    :param b: The second number (float).
    :return: The sum of 'a' and 'b' (float).

    Examples:
    >>> add(3.5, 2.1)
    5.6
    >>> add(10, 5)
    15.0
    >>> add(7.5, 2)
    9.5
    """
    return a + b
