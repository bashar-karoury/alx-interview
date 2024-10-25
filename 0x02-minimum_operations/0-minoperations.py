#!/usr/bin/python3
""" Module that contains minOperations Function """


def getPrimeFactors(n):
    """ Get prime factors """
    factors = []

    # get 2's factors
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    # check odd number from 3 -> ...
    for i in range(3, int(n ** 0.5), 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


def minOperations(n):
    """ Funciton that calculate the fewest number of operations needed to
        result in exactly n H characters given that initially there is a single
        H character and the text editor can execute only two operations in
        the file: CopyAll and Paste.
        Args:
            n: number of H to be represented
        Return: minimum number of operations
    """
    if n == 1:
        return 0
    # get primal factors
    factors = getPrimeFactors(n)
    print("factors ", factors)
    sum = 0
    for factor in factors:
        sum = sum + factor
    return sum
