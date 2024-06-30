# 퇴사 2

"""
P[i] - i일에 잡혀있는 상담을 진행할 때 얻는 수익
T[i] - i일에 잡혀있는 상담을 진행할 때 사용하는 기간

f(n)
-> n일부터 얻을 수 있는 최대 수익
-> max(f(n+1), f(n + T[n]) + P[n])
"""

import sys


input = sys.stdin.readline

N = int(input())

T = []
P = []

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)


def f(n):
    if n == N:
        return 0

    if dp[n] != -1:
        return dp[n]

    dp[n] = f(n + 1)

    # 기간 내에 상담을 할 수 있을 때
    if n + T[n] <= N:
        dp[n] = max(dp[n], f(n + T[n]) + P[n])

    return dp[n]


dp = [-1] * N
print(f(0))
