#!/usr/bin/python3

"""A making change module"""


def count_min_coins(coins, size, sum, db):
    """A function that determines the fewest number of
        coins needed to meet a given amount

    Args:
        coins (list[int]): A list of the available coins
        size (int): The number of coins
        sum (int): The total amount needed
        db (list[list[int]]): A memory for the all previous solutions
    """

    if sum < 0 or size <= 0:
        return 0

    if sum == 0:
        return 1

    if db[size - 1][sum] == -1:
        db[size - 1][sum] =\
            count_min_coins(coins, size, sum - coins[size - 1], db) +\
                count_min_coins(coins, size - 1, sum, db)

    return db[size - 1][sum]


def makeChange(coins, total):
    """A function that makes a memory for the count_min_coins function

    Args:
        coins (list[int]): A list of the available coins
        total (int): The total amount needed

    Returns:
        int: The fewest number of coins needed to meet total
    """

    num_of_coins = len(coins)
    db = [[-1 for _ in range(total + 1)] for _ in range(num_of_coins)]

    return count_min_coins(coins, num_of_coins, total, db)
