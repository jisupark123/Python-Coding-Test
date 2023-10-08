# 팰린드롬?

"""
nums = [1, 2, 1, 3, 1, 2, 1]

1. i == j 이면 팰린드롬 (한글자)
2. nums[i] == nums[j] 이면 
2-1. i - j == 1 이면 팰린드롬 (두글자)
2-2. dp[i][j] = dp[i+1][j-1]
"""

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

dp = [[0] * N for _ in range(N)]  # dp[i][j] -> i부터 j까지 팰린드롬인지

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

for k in range(N - 2):
    for i in range(N - 2 - k):
        j = i + 2 + k
        if nums[i] == nums[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[i - 1][j - 1])
