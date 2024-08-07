#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n H characters in the file.
    """
    if n < 1:
        return 0
    operations, root = 0, 2
    while root <= n:
        if n % root == 0:
            operations += root
            n /= root
            root -= 1
        root += 1
    return operations
