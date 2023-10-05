# 연구소 3

import sys
from collections import deque

input = sys.stdin.readline

EMPTY = 0
WALL = 1
NON_ACTIVATED_VIRUS = 2
ACTIVATED_VIRUS = 3

N, M = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]


non_activated_viruses = []
target_init = 0  # 0 개수

for i in range(N):
    for j in range(N):
        if _map[i][j] == NON_ACTIVATED_VIRUS:
            non_activated_viruses.append((i, j))
        elif _map[i][j] == EMPTY:
            target_init += 1

if target_init == 0:
    print(0)
    exit(0)

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

res = 1e9


# 선택된 바이러스들을 활성으로 만들면 몇초 걸리는지 시뮬레이션
def simulation(choices):
    global res
    visited = [[False] * N for _ in range(N)]
    queue = deque()  # i, j, 걸린 시간(초)
    target = target_init  # 처리해야 할 곳 개수
    for i in choices:
        row, col = non_activated_viruses[int(i)]
        _map[row][col] = ACTIVATED_VIRUS
        queue.append((row, col, 0))
        visited[row][col] = True

    while queue:
        row, col, n = queue.popleft()
        if _map[row][col] == EMPTY:
            target -= 1
            if target == 0:
                res = min(res, n)
                return

        # 상하좌우로 바이러스 퍼뜨리기
        for i in range(4):
            ny = row + dy[i]
            nx = col + dx[i]

            if (
                0 <= ny < N
                and 0 <= nx < N
                and _map[ny][nx] in (EMPTY, NON_ACTIVATED_VIRUS)
                and not visited[ny][nx]
            ):
                visited[ny][nx] = True

                queue.append((ny, nx, n + 1))
    for i in choices:
        row, col = non_activated_viruses[int(i)]
        _map[row][col] = NON_ACTIVATED_VIRUS


def dfs(n: int, choices: str):
    if n == M:
        simulation(choices)
    if int(choices[-1]) == len(non_activated_viruses) - 1:
        return
    for i in range(int(choices[-1]) + 1, len(non_activated_viruses)):
        dfs(n + 1, choices + str(i))


for i in range(len(non_activated_viruses)):
    dfs(1, str(i))

print(res if res != 1e9 else -1)
