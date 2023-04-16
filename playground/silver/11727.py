# 2×n 타일링 2

import sys

sys.setrecursionlimit(10000000)

n = int(input())

res = 0

memo = [-1 for _ in range(n + 1)]


def dfs(i, total):
    if memo[i] != -1:
        return memo[i]
    if i == n:
        return 1
    cnt = dfs(i + 1, total)
    if n - i >= 2:
        a = dfs(i + 2, total)
        cnt += a * 2

    memo[i] = cnt
    return total + cnt


print(dfs(0, 0) % 10007)
