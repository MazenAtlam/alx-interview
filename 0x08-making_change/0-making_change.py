#!/usr/bin/python3

"""A making change module"""

import math


def makeChange(coins, total):
    """A function that makes a memory for the count_min_coins function

    Args:
        coins (list[int]): A list of the available coins
        total (int): The total amount needed

    Returns:
        int: The fewest number of coins needed to meet total
    """

    if total <= 0:
        return 0

    db = [math.inf] * (total + 1)
    db[0] = 0

    for subtotal in range(1, total + 1):
        for coin in coins:
            if subtotal - coin >= 0:
                db[subtotal] = min(db[subtotal], db[subtotal - coin] + 1)

    return db[total] if not math.isinf(db[total]) else -1
