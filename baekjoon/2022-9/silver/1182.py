# 부분수열의 합
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
sequence = list(map(int, input().split()))
res = 0


def dfs(idx, sum):
    global res
    if idx >= n:
        return
    sum += sequence[idx]
    if sum == s:
        res += 1

    dfs(idx + 1, sum - sequence[idx])
    dfs(idx + 1, sum)


dfs(0, 0)

print(res)
