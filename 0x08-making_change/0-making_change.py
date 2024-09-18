#!/usr/bin/python3
"""A module that determines the fewest number of coins needed"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    idx = 0
    while total > 0 and idx < len(coins):
        while total >= coins[idx]:
            total -= coins[idx]
            num_coins += 1
        idx += 1
    return num_coins if total == 0 else -1
