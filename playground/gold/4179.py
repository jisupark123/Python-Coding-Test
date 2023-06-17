# 불!

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

maze = [list(input().strip()) for _ in range(R)]
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

fire = deque()
start = ()

for i in range(R):
    for j in range(C):
        if maze[i][j] == "F":
            fire.append((i, j))
        elif maze[i][j] == "J":
            maze[i][j] = "."
            start = (i, j)

time = 0

while fire:
    i, j = fire.popleft()
    maze[i][j] = time
    for ni, nj in direction:
        if 0 <= i + ni < R and 0 <= j + nj < C and maze[i + ni][j + nj] == ".":
            fire.append((i + ni, j + nj))

    time += 1


res = 1e9

queue = deque()  # (row,col,time)
queue.append((*start, 0))

visited = [[False] * C for _ in range(R)]

while queue:
    i, j, time = queue.popleft()
    if i in (0, R - 1) or j in (0, C - 1):
        res = min(res, time + 1)
        break
    for ni, nj in direction:
        if (
            maze[i + ni][j + nj] != "#"
            and not visited[i + ni][j + nj]
            and maze[i + ni][j + nj] > time + 1
        ):
            visited[i + ni][j + nj] = True
            queue.append((i + ni, j + nj, time + 1))

print(res if res != 1e9 else "IMPOSSIBLE")
