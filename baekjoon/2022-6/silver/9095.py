# 1, 2, 3 더하기

import sys


def dfs(target, total):
    global res
    if total == target:
        res += 1
        return
    if total >= target:
        return
    dfs(target, total + 1)
    dfs(target, total + 2)
    dfs(target, total + 3)


input = sys.stdin.readline
T = int(input())
nums = [int(input()) for _ in range(T)]
for target in nums:
    res = 0
    dfs(target, 0)
    print(res)
