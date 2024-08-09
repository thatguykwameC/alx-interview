#!/usr/bin/python3
"""Determines the number of minmum operations given n characters"""


def minOperations(n):
    """
    Calculate the minimum number of operations
    needed to reach a given number `n`.

    Parameters:
        n (int): The target number to reach.

    Returns:
        int: The minimum number of operations needed to reach `n`.
    """
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter
