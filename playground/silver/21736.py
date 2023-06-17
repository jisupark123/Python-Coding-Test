# 헌내기는 친구가 필요해

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

EMPTY = "O"
WALL = "X"
PERSON = "P"

campas = [input().strip() for _ in range(N)]

location = ()

for i in range(N):
    for j in range(M):
        if campas[i][j] == "I":
            location = (i, j)
            break

cnt = 0

visited = [[False] * M for _ in range(N)]
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

queue = deque()
queue.append(location)

while queue:
    i, j = queue.popleft()
    if campas[i][j] == PERSON:
        cnt += 1
    for d in direction:
        next_i = i + d[0]
        next_j = j + d[1]
        if (
            0 <= next_i < N
            and 0 <= next_j < M
            and not visited[next_i][next_j]
            and campas[next_i][next_j] != WALL
        ):
            visited[next_i][next_j] = True
            queue.append((next_i, next_j))

print(cnt if cnt > 0 else "TT")
