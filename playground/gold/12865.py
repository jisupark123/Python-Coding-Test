# 평범한 배낭

"""
sol(K,N) = max(things[0][1] + sol(K - things[0][0], N-1))
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

things = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)

for i in range(N):
    dp[i] = max(things[i][1] + dp[2])


def sol(w, i):
    max_v = 0
    for idx in range(i - 1, -1, -1):
        if w - things[idx][0] >= 0:
            max_v = max(max_v, things[idx][1] + sol(w - things[idx][0], idx))
    return max_v


# print(sol(K, N))
