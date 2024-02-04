# 다리 만들기

"""
1. 섬을 구분하기 위해 섬마다 각각 다른 식별자를 붙인다. (식별자 -> 1~, BFS 수행)
2. 섬을 구성하고 있는 좌표를 모두 큐에 넣는다. 효율을 위해 가장 많은 부피를 가진 섬은 제외한다. (하나는 제외해도 결과가 나옴)
3. BFS를 통해 섬을 연결시키는 탐색을 수행한다. 가장 먼저 찾는 좌표가 정답
"""

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


# 섬을 구분하기 위해 섬마다 각각 다른 식별자를 붙인다.
# 가장 큰 해시를 가진 섬의 해시를
def hash_to_map():

    hash = 2  # 섬이 1로 되어있으므로 해시값은 2부터
    visited = [[0] * N for _ in range(N)]
    save_cnt = defaultdict(int)

    for i in range(N):
        for j in range(N):
            if _map[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                _map[i][j] = hash
                save_cnt[hash] += 1

                while queue:
                    y, x = queue.popleft()
                    for a in range(4):
                        ny, nx = y + dy[a], x + dx[a]
                        if (
                            in_range(ny, nx)
                            and not visited[ny][nx]
                            and _map[ny][nx] == 1
                        ):
                            visited[ny][nx] = 1
                            _map[ny][nx] = hash
                            save_cnt[hash] += 1
                            queue.append((ny, nx))

                hash += 1

    return max([[save_cnt[k], k] for k in save_cnt.keys()])[1]


N = int(input())

_map = [list(map(int, input().split())) for _ in range(N)]

in_range = lambda y, x: 0 <= y < N and 0 <= x < N

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

max_hash = hash_to_map()

# 섬을 구성하고 있는 좌표를 모두 큐에 넣는다. 효율을 위해 가장 많은 부피를 가진 섬은 제외한다.

# visited[i][j] -> i, j에 방문했던 hash값
visited = [[set() for _ in range(N)] for _ in range(N)]
queue = deque()  # y, x, 다리 길이, hash

for i in range(N):
    for j in range(N):
        if _map[i][j] not in (0, max_hash):
            queue.append((i, j, 0, _map[i][j]))

# BFS를 통해 섬을 연결시키는 탐색을 수행한다. 가장 먼저 찾는 좌표가 정답

while queue:
    y, x, bridge_cnt, hash = queue.popleft()

    if _map[y][x] not in (0, hash):
        print(bridge_cnt - 1)
        break

    for a in range(4):
        ny, nx = y + dy[a], x + dx[a]

        if in_range(ny, nx) and hash not in visited[ny][nx] and _map[ny][nx] != hash:
            visited[ny][nx].add(hash)
            queue.append((ny, nx, bridge_cnt + 1, hash))
