# 빙산

# 배열을 순회하면서 빙산을 깍는다.
# 다만 완전히 녹는(0이 되는) 빙산은 따로 리스트에 저장해 놨다가 한 번에 없앤다(다른 빙산에 영향을 줌)
# 배열을 순회하면서 bfs로 빙산이 몇 조각인지 센다.
# 2조각 이상이면 끝
# 1조각이면 시간 += 1

# 최적화 -> 매턴마다 배열을 순회하지 않고 ice들을 set으로 관리

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

ice_map = [list(map(int, input().split())) for _ in range(N)]
ice_set = set()
for i in range(N):
    for j in range(M):
        if ice_map[i][j] != 0:
            ice_set.add((i, j))


time = 1

# 4방향
# ← ↑ → ↓
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]


def count_melt(i, j):
    cnt = 0
    for d in direction:
        if ice_map[i + d[0]][j + d[1]] == 0:
            cnt += 1
    return cnt


def count_partition():
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(M):
            if ice_map[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                queue.append((i, j))
                res += 1
                while queue:
                    n, m = queue.popleft()
                    for d in direction:
                        if (
                            ice_map[n + d[0]][m + d[1]] != 0
                            and not visited[n + d[0]][m + d[1]]
                        ):
                            visited[n + d[0]][m + d[1]] = True
                            queue.append((n + d[0], m + d[1]))

    return res


while True:
    will_zero = []
    for i, j in ice_set:
        melting = count_melt(i, j)
        if ice_map[i][j] - melting > 0:
            ice_map[i][j] -= melting
        elif ice_map[i][j] - melting <= 0:
            will_zero.append((i, j))
    for i, j in will_zero:
        ice_map[i][j] = 0
        ice_set.discard((i, j))

    partition = count_partition()
    if partition > 1:
        print(time)
        break
    if len(ice_set) == 0:
        print(0)
        break
    time += 1
