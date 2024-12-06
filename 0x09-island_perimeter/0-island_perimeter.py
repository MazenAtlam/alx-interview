#!/usr/bin/python3

"""An island perimeter module"""

def square_perimeter(grid, no_rows, no_columns, row, column):
    perimeter = 0
    grid[row][column] = -1

    if row < no_rows - 1:
        if grid[row + 1][column] == 0:
            perimeter += 1

        elif grid[row + 1][column] == 1:
            perimeter += square_perimeter(grid, no_rows, no_columns, row + 1, column)
    else:
        perimeter += 1

    if column < no_columns - 1:
        if grid[row][column + 1] == 0:
            perimeter += 1

        elif grid[row][column + 1] == 1:
            perimeter += square_perimeter(grid, no_rows, no_columns, row, column + 1)
    else:
        perimeter += 1

    if row > 0:
        if grid[row - 1][column] == 0:
            perimeter += 1
        elif grid[row - 1][column] == 1:
            perimeter += square_perimeter(grid, no_rows, no_columns, row - 1, column)
    else:
        perimeter += 1

    if column > 0:
        if grid[row][column - 1] == 0:
            perimeter += 1
        elif grid[row][column - 1] == 1:
            perimeter += square_perimeter(grid, no_rows, no_columns, row, column - 1)
    else:
        perimeter += 1

    return perimeter


def island_perimeter(grid):
    no_rows = len(grid)
    if no_rows <= 0:
        return 0

    no_columns = len(grid[0])
    if no_columns <= 0:
        return 0

    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if grid[row][column] == 1:
                return square_perimeter(grid, no_rows, no_columns, row, column)

    return 0


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(island_perimeter(grid))
    grid = [[1]]
    print(island_perimeter(grid))
    grid = [[1, 0]]
    print(island_perimeter(grid))
    grid = [[1, 1], [1, 1]]
    print(island_perimeter(grid))
