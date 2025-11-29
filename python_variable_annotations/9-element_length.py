#!/usr/bin/env python3
"""
List utilities module.

This module provides functions to analyze elements in iterable sequences.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples where each tuple contains an element from the
    input and its length.

    :param lst: An iterable of sequences (like strings or lists).
    :return: A list of tuples (element, length of element).

    Examples:
    >>> element_length(["hello", "world"])
    [('hello', 5), ('world', 5)]
    >>> element_length(["", "a"])
    [('', 0), ('a', 1)]
    """
    return [(i, len(i)) for i in lst]
