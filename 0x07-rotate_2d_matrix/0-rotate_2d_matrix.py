#!/usr/bin/python3

"""Rotating a 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D Matrix 90 degrees clockwise"""
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
