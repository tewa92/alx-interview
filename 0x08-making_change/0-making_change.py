#!/usr/bin/python3

""" Minimum coins """

def makeChange(coins, total):
    if total <= 0:
        return 0
    minCoins = [total + 1] * (total + 1)
    minCoins[0] = 0
    for i in range(total + 1):
        for coin in coins:
            if coin <= i:
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)
    if minCoins[total] > total:
        return -1
    return minCoins[total]
