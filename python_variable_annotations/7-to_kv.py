#!/usr/bin/env python3
"""
Key-value utilities module.

This module provides functions to create key-value pairs with processed values.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple of a string key and the square of a number as a float.

    :param k: The key as a string.
    :param v: An int or float value.
    :return: A tuple (k, v squared as float).

    Examples:
    >>> to_kv("eggs", 3)
    ('eggs', 9.0)
    >>> to_kv("school", 0.02)
    ('school', 0.0004)
    """
    return (k, float(v ** 2))
