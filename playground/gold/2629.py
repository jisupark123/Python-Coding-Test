# 양팔저울

"""
각각의 추를 더하거나/빼거나/계산에 포함하지 않고 무게(a)를 만들 수 있나

w <- 추 list

추가 순서대로 나열되어 있을 때
f(i, k)
-> i번째 추까지 고려했고 이전에 누적된 값이 k일 때, 무게 a를 만들 수 있는지
-> f(i+1, k+w[i]) or f(i+1, k-w[i]) or f(i+1, k)
"""

import sys

input = sys.stdin.readline

N = int(input())

w = list(map(int, input().split()))


def dfs(i, k):
    if i == N:
        return k == target

    if dp[i][k] != -1:
        return dp[i][k]

    dp[i][k] = dfs(i + 1, k + w[i]) or dfs(i + 1, k - w[i]) or dfs(i + 1, k)
    return dp[i][k]


int(input())
targets = list(map(int, input().split()))
for target in targets:
    dp = [[-1] * (N * 500) for _ in range(N)]
    print("Y" if dfs(0, 0) else "N", end=" ")
