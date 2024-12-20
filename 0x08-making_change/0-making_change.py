#!/usr/bin/python3
"""  Change comes from within """


def makeChange(coins, total):
    """ returns the fewest number of coins needed to meet a given amount total
    """

    if not coins:
        return -1
    if total <= 0:
        return 0
    # initialize result with -1
    result = 0

    # sort coins
    coins.sort(reverse=True)

    # start wit greatest coin
    # current_idx = 0
    idx = 0
    current_coin = coins[idx]

    # print('coins: ', coins)
    if total < coins[-1]:
        return -1

    while (total > 0 and idx < len(coins)):
        if total >= coins[idx]:
            total -= coins[idx]
            result += 1
            # print(f'total: {total}, coin: {coins[idx]}, result-now {result}')
            continue
        else:
            idx += 1

    if total == 0:
        return result
    else:
        return -1
