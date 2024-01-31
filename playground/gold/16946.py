# 벽 부수고 이동하기 4

"""
모든 빈곳에 대해 이동할 수 있는 칸의 개수를 세어놓는다.
다만 중복될 수 있으므로 연결된 빈곳은 같은 해시값을 붙인다.
"""

import sys
from collections import deque

input = sys.stdin.readline


# i,j와 인접한 좌표 모두 반환 (i,j 포함)
def get_neighbors(i, j):
    res = [(i, j)]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        y, x = queue.popleft()
        for a in range(4):
            ny, nx = y + dy[a], x + dx[a]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and not visited[ny][nx]
                and _map[ny][nx] == 0
            ):
                visited[ny][nx] = 1
                queue.append((ny, nx))
                res.append((ny, nx))

    return res


N, M = map(int, input().split())

_map = [list(map(int, list(input().strip()))) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

hash = 0

for i in range(N):
    for j in range(M):
        if _map[i][j] == 0 and not visited[i][j]:
            neighbors = get_neighbors(i, j)
            len_neighbors = len(neighbors)
            for y, x in neighbors:
                dp[y][x] = (hash, len_neighbors)

            hash += 1


for i in range(N):
    for j in range(M):
        if _map[i][j] == 1:
            s = set()
            v = 1
            for a in range(4):
                ni, nj = i + dy[a], j + dx[a]
                if 0 <= ni < N and 0 <= nj < M and dp[ni][nj] != 0:
                    _hash, cnt = dp[ni][nj]
                    if _hash not in s:
                        s.add(_hash)
                        v += cnt
            _map[i][j] = v % 10


for i in range(N):
    for j in range(M):
        print(_map[i][j], end="")
    print()
