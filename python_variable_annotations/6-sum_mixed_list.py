#!/usr/bin/env python3
"""
List utilities module.

This module provides functions for working with lists of integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a list containing integers and floats.

    :param mxd_lst: A list of ints and floats.
    :return: The sum of all elements as a float.

    Examples:
    >>> sum_mixed_list([1, 2.5, 3])
    6.5
    """
    return sum(mxd_lst)
