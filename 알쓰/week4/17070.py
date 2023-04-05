# 파이프 옮기기 1

# 가로 0 세로 1 대각선 2

import sys

input = sys.stdin.readline
N = int(input())

home = [list(map(int, input().split())) for _ in range(N)]

res = 0
direction = [(1, 0), (1, 1), (0, 1)]

memo = [[[-1 for _ in range(N)] for _ in range(N)] for _ in range(3)]


def check(i, j):
    if 0 <= i < N and 0 <= j < N and home[i][j] == 0:
        return True
    return False


def to_right(i, j):
    next_i = i
    next_j = j + 1
    if check(next_i, next_j):
        return dfs(0, next_i, next_j)
    return 0


def to_bottom(i, j):
    next_i = i + 1
    next_j = j
    if check(next_i, next_j):
        return dfs(1, next_i, next_j)
    return 0


def to_diagonal(i, j):
    next_i = i + 1
    next_j = j + 1
    if check(next_i, next_j) and check(i + 1, j) and check(i, j + 1):
        return dfs(2, next_i, next_j)
    return 0


# 가로 0 세로 1 대각선 2
def dfs(status, i, j):
    if i == N - 1 and j == N - 1:
        return 1

    if memo[status][i][j] != -1:
        return memo[status][i][j]

    cnt = 0

    if status == 0:
        cnt = to_right(i, j) + to_diagonal(i, j)
    elif status == 1:
        cnt = to_bottom(i, j) + to_diagonal(i, j)
    elif status == 2:
        cnt = to_right(i, j) + to_bottom(i, j) + to_diagonal(i, j)

    memo[status][i][j] = cnt
    return cnt


print(dfs(0, 0, 1))
