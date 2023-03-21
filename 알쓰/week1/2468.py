# 안전 영역

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline
N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
res = 1  # 최대 개수

for height in range(1, 100):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0

    def dfs(y, x, h):
        visited[y][x] = True
        for d in direction:
            next_y = y + d[0]
            next_x = x + d[1]
            if (
                0 <= next_y < N
                and 0 <= next_x < N
                and not visited[next_y][next_x]
                and lst[next_y][next_x] > h
            ):
                dfs(next_y, next_x, h)

    for y in range(N):
        for x in range(N):

            # 높이가 빗물 높이 이하라면
            if lst[y][x] > height and not visited[y][x]:
                dfs(y, x, height)
                cnt += 1
    res = max(cnt, res)

print(res)
