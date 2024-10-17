#!/usr/bin/env python3

"""Minimum Operations Module."""


def minOperations(n):
    """Gets the minimum number of operations to write n of 'H' in a text file.
    Only (Copy All - Paste) operations are allowed.

    Args:
        n (int): The number of 'H' to be written

    Returns:
        int: Minimum number of operations required
    """

    if n < 2:
        return 0

    num_op = 2
    num_H = 2
    copied = 1

    while (num_H < n):
        if n % num_H == 0:
            copied = num_H
            num_op += 1

        num_H += copied
        num_op += 1

    if num_H != n:
        return 0

    return num_op
