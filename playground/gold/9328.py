# 열쇠

"""
BFS

- 획득한 key는 전역으로 관리
- 탐색 중 키가 없어서 막힌다면 위치 save 후 해당 키 획득 시 다시 queue에 삽입 (key에 따른 위치들은 해시테이블로 관리)
- 한 번 방문했던 곳은 다시 방문 X
"""

import sys
from collections import deque, defaultdict


input = sys.stdin.readline


for _ in range(int(input())):

    h, w = map(int, input().split())

    _map = [list(input().strip()) for _ in range(h)]

    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    keys = set(list(input().strip()))
    if "0" in keys:
        keys = set()

    entries = []  # 입구

    for i in range(h):
        for j in range(w):
            if _map[i][j] != "*" and (i in (0, h - 1) or j in (0, w - 1)):
                entries.append((i, j))

    # 탐색 중 키가 없어서 막힌다면 위치 save 후 해당 키 획득 시 다시 queue에 삽입
    # key - 열쇠(소문자)
    # value - list(위치) (같은 문이 여러개 있을 수 있음)
    respawn = defaultdict(list)
    visited = [[0] * w for _ in range(h)]
    queue = deque()

    ans = 0  # 찾은 문서 개수

    # 입구로 가기 전 좌표를 queue에 추가
    for y, x in entries:
        if y == 0:
            queue.append((y - 1, x))
        elif y == h - 1:
            queue.append((y + 1, x))
        elif x == 0:
            queue.append((y, x - 1))
        else:
            queue.append((y, x + 1))

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (
                0 <= ny < h
                and 0 <= nx < w
                and _map[ny][nx] != "*"
                and not visited[ny][nx]
            ):
                if _map[ny][nx] == ".":
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

                elif _map[ny][nx] == "$":
                    ans += 1
                    _map[ny][nx] = "."
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

                elif _map[ny][nx] == _map[ny][nx].lower():
                    key = _map[ny][nx]
                    keys.add(key)
                    _map[ny][nx] = "."
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

                    for ay, ax in respawn[key]:

                        if not visited[ay][ax]:
                            _map[ay][ax] = "."
                            visited[ay][ax] = 1
                            queue.append((ay, ax))

                else:  # 대문자(문)
                    key = _map[ny][nx].lower()
                    if key in keys:
                        _map[ny][nx] = "."
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                    else:
                        respawn[key].append((ny, nx))

    print(ans)
