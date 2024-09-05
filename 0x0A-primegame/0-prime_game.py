#!/usr/bin/python3
""" Prime Game module
"""


def isWinner(x, nums):
    """ Determines the winner of the Prime Geme.
    There are always two players at all times

    Args:
        x(int): number of rounds
        nums(list): an array of n
    """
    if x is None or nums is None or x <= 0 or nums == []:
        return None

    def sieve_of_eratosthenes(n):
        """ Helper returns a list of primes up to n
        using the Sieve of Eratosthenes

        Args:
            n(int): limit
        Returns:
            list: where True indicates that the index is a prime number
        """
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False
        return sieve

    max_n = max(nums)
    prime_flags = sieve_of_eratosthenes(max_n)

    maria_wins, ben_wins = 0, 0

    for n in nums:
        prime_count = sum(prime_flags[2:n + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
