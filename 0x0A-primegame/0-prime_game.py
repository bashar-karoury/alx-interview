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
    while (i < x):
        # all initially primes
        # print(f'Selecting num {nums[i]}')
        lst = [True for i in range(0, nums[i] + 1)]
        lst[0] = False
        lst[1] = False
        # alternate turns till all lst is False
        turn = 1
        while True in lst:
            turn = not turn
            turner = 'Maria' if not turn else 'Ben'
            # print(f'turn of {turner}')
            # get first True idx = 2
            idx = lst.index(True)
            # print(f'first idx {idx}')
            lst[idx] = False
            # Falsify all multiples
            for idx in range(idx * 2, len(lst), idx):
                lst[idx] = False
            # print(lst)
        score[turn] += 1
        turner = 'Maria' if not turn else 'Ben'
        # print(f'Winner is {turner}')
        i += 1
    # print('score', score)
    if score[0] > score[1]:
        return "Maria"
    elif score[1] > score[0]:
        return "Ben"
    else:
        return None
