# 토마토


def bfs(idx_i, idx_j):
    queue: deque[list[int]] = deque()
    queue.append([idx_i, idx_j])
    while len(queue) != 0:
        i, j = queue.popleft()
        for d in directions:

            # 원래 위치로 돌아오면
            if i + d[0] == idx_i and j + d[1] == idx_j:
                continue

            if (
                0 <= i + d[0] < n
                and 0 <= j + d[1] < m
                and box[i + d[0]][j + d[1]] != -1
                and (
                    box[i + d[0]][j + d[1]] == 0
                    or box[i + d[0]][j + d[1]] > box[i][j] + 1
                )
            ):
                box[i + d[0]][j + d[1]] = box[i][j] + 1
                queue.append([i + d[0], j + d[1]])


from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            bfs(i, j)
for b in box:
    print(b)


def get_res():
    res = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
            res = max(res, box[i][j])
    return res - 1


print(get_res())
