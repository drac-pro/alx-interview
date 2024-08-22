#!/usr/bin/python3
""" making_change module
"""
import sys


def makeChange(coins, total):
    """ determine the fewest number of coins needed to meet a
    given amount total from a pile of coins

    Args:
        coins (list): list of values(coins)
        total (int): the total change to make
    Returns:
        int: the smallest number of coins needed or 0 otherwise
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    remaining_amount = total
    
    for coin in coins:
        if remaining_amount == 0:
            break

        count = remaining_amount // coin
        num_coins += count
        remaining_amount -= count * coin

    return num_coins if remaining_amount == 0 else -1
