#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    function to return pascal triangle of n
    """
    result = []
    if n <= 0:
        return result
    result.append([1])
    for i in range(1, n):
        row = []
        for j in range(i + 1):
            a = result[i-1][j] if not (j > i - 1) else 0
            b = result[i-1][j-1] if not (j - 1 < 0) else 0
            row.append(a + b)
        result.append(row)
    return result
