#!/usr/bin/python3
"""A model to generate Pascal’s triangle of n"""


def pascal_triangle(n):
    """A function returns a list of lists of integers
        representing the Pascal’s triangle of n

    Args:
        n (int): The number of rows of Pascal’s triangle

    Returns:
        list: A list of lists of integers representing
        the Pascal’s triangle of n
    """

    if n <= 0:
        # Return an empty list if n is less than or equal to 0
        return []

    pascal_tri = [] # Initialize the Pascal’s triangle

    for row_index in range(n):
        # Generate a new row of Pascal’s triangle
        row = [1] # Initialize the first integer of the row always to 1

        for col_index in range(1, row_index):
            # Each integer in the row is follow the formula:
            # pascal_tri[i][j] = pascal_tri[i-1][j] + pascal_tri[i-1][j-1]
            row.append(pascal_tri[-1][col_index] + pascal_tri[-1][col_index - 1])

        # The last integer of the row always to 1 if i is not 0
        if row_index != 0:
            row.append(1)

        pascal_tri.append(row) # Append the row to the Pascal’s triangle

    return pascal_tri # Return the Pascal’s triangle
