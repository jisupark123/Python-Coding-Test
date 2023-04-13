# 연구소

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

BLACK = 0
WALL = 1
VIRUS = 2

_map = []
viruses = []

for i in range(N):
    lst = []
    for j, n in enumerate(map(int, input().split())):
        lst.append(n)
        if n == VIRUS:
            viruses.append((i, j))
    _map.append(lst)


def n_to_idx(n):
    i = (n - 1) // M
    j = (n - 1) - (i * M)
    return (i, j)


direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def safe_area_count():
    queue = deque(viruses)
    visit = [[False for _ in range(M)] for _ in range(N)]
    while queue:
        i, j = queue.popleft()
        for d in direction:
            next_i = i + d[0]
            next_j = j + d[1]
            if (
                0 <= next_i < N
                and 0 <= next_j < M
                and not visit[next_i][next_j]
                and _map[next_i][next_j] == 0
            ):
                visit[next_i][next_j] = True
                queue.append((next_i, next_j))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and _map[i][j] == 0:
                cnt += 1

    return cnt


res = 0
for a, b, c in combinations(range(N * M), 3):
    a1, a2 = n_to_idx(a)
    b1, b2 = n_to_idx(b)
    c1, c2 = n_to_idx(c)
    if _map[a1][a2] != 0 or _map[b1][b2] != 0 or _map[c1][c2] != 0:
        continue
    _map[a1][a2] = 1
    _map[b1][b2] = 1
    _map[c1][c2] = 1

    cnt = safe_area_count()
    res = max(res, cnt)
    _map[a1][a2] = 0
    _map[b1][b2] = 0
    _map[c1][c2] = 0

print(res)
