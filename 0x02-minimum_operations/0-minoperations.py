#!/usr/bin/python3
"""defines a function minOperations(n)"""


def minOperations(n):
    """calculates the fewest number of operations needed to result in exactly
    n H characters in the file.
    Args:
        n(int): number of times the char 'H' must appear in the text file
    Returns:
        int: the minimum number of operations(Copy All and Paste) to get n * H
    """
    if n <= 1:
        return 0
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
