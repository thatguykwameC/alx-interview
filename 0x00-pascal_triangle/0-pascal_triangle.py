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
    if col == 0 or col == row:
        return 1

    return Calc(row - 1, col - 1) + Calc(row - 1, col)


def pascal_triangle(n):
    if n <= 0:
        return []

    p_triangle = []
    for i in range(n):
        row = [Calc(i, j) for j in range(i + 1)]
        p_triangle.append(row)
    return p_triangle
