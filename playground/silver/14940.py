# 쉬운 최단거리


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(n)]

start = ()
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
for i in range(n):
    for j in range(m):
        if _map[i][j] == 2:
            start = (i, j)


res = [[0] * m for _ in range(n)]
queue = deque()
queue.append((*start, 0))

while queue:
    i, j, distance = queue.popleft()
    for d in direction:
        next_i = i + d[0]
        next_j = j + d[1]
        if (
            0 <= next_i < n
            and 0 <= next_j < m
            and res[next_i][next_j] == 0
            and _map[next_i][next_j] not in (2, 0)
        ):
            res[next_i][next_j] = distance + 1
            queue.append((next_i, next_j, distance + 1))


for i in range(n):
    for j in range(m):
        if _map[i][j] != 0 and res[i][j] == 0 and (i, j) != start:
            res[i][j] = -1

for r in res:
    print(*r)
