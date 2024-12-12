#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """
    function to determine the name of winner of prime game
    Args:
        x: is the number of rounds.
        nums is an array of n.
        Return: name of the player that won the most rounds
            If the winner cannot be determined, return None
    """
    if x < 1:
        return None
    if x > len(nums):
        return None
    if not nums:
        return None
    if not isinstance(nums, list):
        return None
    score = [0, 0]
    i = 0

    max_n = max(nums)

    lst = [True for i in range(0, max_n + 1)]
    lst[0] = False
    lst[1] = False
    for i in range(len(lst)):
        # print('i ',i)
        if lst[i]:
            for idx in range(i * 2, len(lst), i):
                lst[idx] = False
    # print(lst)
    for _ in range(x):
        # get primes till nums[_]
        primes = list(filter(lambda y: lst[y], range(2, nums[_] + 1)))
        if len(primes) % 2 == 0:
            score[1] += 1
        else:
            score[0] += 1
    # print('score', score)
    if score[0] > score[1]:
        return "Maria"
    elif score[1] > score[0]:
        return "Ben"
    else:
        return None
