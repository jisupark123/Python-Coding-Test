# 동전 1

"""
동전 - n1,...,ni
k의 경우의 수 -> k-n1,...,k-ni의 총합

[0,1,2,2,3,4,5]
"""

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])
