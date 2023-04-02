# 테트로미노

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
_max = 0


def dfs(cnt, total, prev, curr):
    global _max
    if cnt == 4:
        _max = max(_max, total)
        return
    for d in direction:
        next_y = curr[0] + d[0]
        next_x = curr[1] + d[1]
        if (
            0 <= next_y < N
            and 0 <= next_x < M
            and (next_y != prev[0] or next_x != prev[1])
        ):
            dfs(cnt + 1, total + paper[next_y][next_x], curr, (next_y, next_x))
    if cnt == 2:
        for d1, d2 in combinations(direction, 2):
            next_d1 = (curr[0] + d1[0], curr[1] + d1[1])
            next_d2 = (curr[0] + d2[0], curr[1] + d2[1])
            if (
                0 <= next_d1[0] < N
                and 0 <= next_d1[1] < M
                and (next_d1[0] != prev[0] or next_d1[1] != prev[1])
                and 0 <= next_d2[0] < N
                and 0 <= next_d2[1] < M
                and (next_d2[0] != prev[0] or next_d2[1] != prev[1])
            ):
                new_total = (
                    total
                    + paper[next_d1[0]][next_d1[1]]
                    + paper[next_d2[0]][next_d2[1]]
                )
                _max = max(_max, new_total)


for y in range(N):
    for x in range(M):
        dfs(1, paper[y][x], (-1, -1), (y, x))

print(_max)
