#!/usr/bin/python3
""" Pascal's Triangle """


def Calc(row, col):
    """
    Recursive call to calculate rows and columns.

    Args:
        row (int): The row index.
        col (int): The column index.

    Returns:
        int: The value at the given row and column.
    """
    # Base case: If it's the first or last column in a row, return 1
    if col == 0 or col == row:
        return 1

    # Recursive case: Calculate by adding the values of the previous row
    return Calc(row - 1, col - 1) + Calc(row - 1, col)


def pascal_triangle(n):
    if n <= 0:
        return []

    p_triangle = []
    for i in range(n):
        row = [Calc(i, j) for j in range(i + 1)]
        # Each row is a list of elements calculated using recursion
        p_triangle.append(row)
    return p_triangle
