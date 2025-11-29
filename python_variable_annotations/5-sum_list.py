#!/usr/bin/env python3
"""
List utilities module.

This module provides simple functions for working with lists of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floating-point numbers.

    :param input_list: A list of floats.
    :return: The sum of all elements in the list as a float.

    Examples:
    >>> sum_list([1.0, 2.5])
    3.5
    """
    return sum(input_list)
