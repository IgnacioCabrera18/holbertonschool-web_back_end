#!/usr/bin/env python3
"""
String utilities module.

This module provides simple functions for basic string operations.
It currently includes the 'concat' function for joining two strings.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatenate two strings.

    Takes two strings and returns a new string that joins them in the
    given order.

    :param str1: The first string.
    :param str2: The second string.
    :return: The concatenation of 'str1' and 'str2'.

    Examples:
    >>> concat("Hello, ", "world")
    'Hello, world'
    >>> concat("foo", "bar")
    'foobar'
    >>> concat("", "test")
    'test'
    """
    return str1 + str2
