# 자두나무

"""
f(t, w)
-> t초가 진행되었고 이미 w번 움직였을 때, 얻을 수 있는 자두의 최대 개수
-> max(f(t+1, w+1), f(t+1, w))
-> 움직이거나 움직이지 않거나
"""

import sys

input = sys.stdin.readline

T, W = map(int, input().split())

plums = list(int(input()) for _ in range(T))

dp = [[-1] * (W + 1) for _ in range(T)]


def dfs(t, w):
    p = 1 if w % 2 == 0 else 2
    curr = 1 if plums[t] == p else 0

    if t == T - 1:
        return curr

    if dp[t][w] != -1:
        return dp[t][w]

    dp[t][w] = curr + dfs(t + 1, w)
    if w < W:
        dp[t][w] = max(dp[t][w], curr + dfs(t + 1, w + 1))

    return dp[t][w]


print(max(dfs(0, 0), dfs(0, 1)))
