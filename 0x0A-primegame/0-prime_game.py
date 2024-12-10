#!/usr/bin/python3

"""A module for the prime game"""


def isWinner(x, nums):
    """A function that determines who the winner of each game in nums is.
    The players are Maria and Ben.
    Maria always starts first.

    Args:
        x (int): The number of rounds.
        nums (list[int]): An array of the value of n in each round.

    Returns:
        The name of the player that won the most rounds,
        or None if the winner cannot be determined.
    """

    # Determine what are the prime numbers from 0 to max_num in nums
    # Sieve of Eratosthenes
    max_num = max(nums)

    count_primes = [1] * (max_num + 1)

    count_primes[0] = count_primes[1] = 0

    for num in range(2, max_num + 1):
        if count_primes[num] == 1:
            for prime_factor in range(2 * num, max_num, num):
                count_primes[prime_factor] = 0

    # Prefix sun of the array to count the primes before each number
    for num in range(3, max_num + 1):
        count_primes[num] += count_primes[num - 1]

    # Start the game
    rounds = x
    maria_wins = ben_wins = 0
    while (x):
        n = nums[rounds - x]

        switches = count_primes[n]

        # Start the round
        winner = False
        # winner is False => Ben wins
        # winner is True => Maria wins
        while (switches):
            winner = not winner
            switches -= 1

        # Who is the winner of this round
        if winner:
            maria_wins += 1
        else:
            ben_wins += 1

        x -= 1

    if ben_wins > maria_wins:
        return "Ben"

    if maria_wins > ben_wins:
        return "Maria"

    return None
