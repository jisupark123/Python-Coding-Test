# 내리막 길

#

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
memo = [[-1] * M for _ in range(N)]
memo[N - 1][M - 1] = 1


def dfs(i, j):
    if memo[i][j] != -1:
        return memo[i][j]

    cnt = 0
    for n_i, n_j in direction:
        if (
            0 <= i + n_i < N
            and 0 <= j + n_j < M
            and _map[i][j] > _map[i + n_i][j + n_j]
        ):
            cnt += dfs(i + n_i, j + n_j)

    memo[i][j] = cnt

    return cnt


print(dfs(0, 0))
