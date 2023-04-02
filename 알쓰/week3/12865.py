# 평범한 배낭

import sys

input = sys.stdin.readline

N, max_weight = map(int, input().split())

bags = [list(map(int, input().split())) for _ in range(N)]
memo = []  # 해당 가방이 쓰였는지 -> memo[i] == True
res = 0


def dfs(n, start_idx, total_weight, total_value):
    global res, memo

    if n == 0:
        memo = [False] * 101
    if n == N - 1:
        res = max(res, total_value)
