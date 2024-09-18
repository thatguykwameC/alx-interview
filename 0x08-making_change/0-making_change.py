#!/usr/bin/python3
"""Module for making change"""


def make_change(coins, total):
    """
    Determine the fewest number of coins needed to
    make change to meet a given amount total
    """
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        num_coins += total // coin
        total %= coin

    return num_coins if total == 0 else -1
