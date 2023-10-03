"""
visited -> 전장[i][j]를 방문했는지 여부
1. 모든 전장을 순회하면서 방문하지 않은 곳은 bfs() 함수를 실행한다.
2. bfs() -> 방문하지 않았던 인접한 전장을 돌면서 서로 인접한 병사의 수를 계산한다. 전장을 방문할 때마다 visited를 업데이트한다.
3. 계산을 마치면 병사의 수 ** 2 를 결과에 포함한다.
"""

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

war = [input().strip() for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    color = war[i][j]
    cnt = 1
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if (
                0 <= ny < n
                and 0 <= nx < m
                and not visited[ny][nx]
                and war[ny][nx] == color
            ):
                cnt += 1
                visited[ny][nx] = True
                queue.append((ny, nx))
    return (color, cnt)


blue, white = 0, 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            color, cnt = bfs(i, j)
            if color == "B":
                blue += cnt**2
            else:
                white += cnt**2

print(white, blue)
