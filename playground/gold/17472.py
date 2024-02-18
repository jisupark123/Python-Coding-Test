# 다리 만들기 2

"""
1. 섬마다 고유한 숫자(해시)를 붙인다.
2. 바다와 접한 섬의 외각마다 다리를 생성해서 큐에 넣는다.
3. BFS로 위에서 생성한 다리들을 완성시킨다. 이 때 길이가 1인 다리는 탈락시키고, 중복을 방지하기 위해 숫자가 낮은 섬에서 높은 섬으로 가는 다리만 남긴다.
4. DFS로 경우의 수를 탐색하면서 모든 섬을 연결하는 다리 길이의 최솟값을 구한다. 다리의 개수는 모든 섬의 개수 - 1 이다.
"""

import sys
from collections import deque
import heapq

input = sys.stdin.readline


# 섬을 구분하기 위해 섬마다 각각 다른 식별자를 붙인다.
# 섬의 종류의 개수를 return
def hash_to_island():

    hash = 2  # 섬이 1로 되어있으므로 해시값은 2부터
    visited = [[0] * M for _ in range(N)]
    island_cnt = 0

    for i in range(N):
        for j in range(M):
            if _map[i][j] == 1 and not visited[i][j]:
                visited[i][j] = 1
                queue = deque()
                queue.append((i, j))
                _map[i][j] = hash

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
                            queue.append((ny, nx))

                hash += 1
                island_cnt += 1

    return island_cnt


N, M = map(int, input().split())

_map = [list(map(int, input().split())) for _ in range(N)]

in_range = lambda y, x: 0 <= y < N and 0 <= x < M

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 1. 섬마다 고유한 숫자(해시)를 붙인다.
island_cnt = hash_to_island()


# 2. 바다와 접한 섬의 외각마다 다리를 생성해서 큐에 넣는다.
queue = deque()  # (y, x, 다리 길이, 출발한 섬, 방향y, 방향x)

for y in range(N):
    for x in range(M):

        # 섬이라면 4방향 모두 검사 -> 바다라면 다리 생성
        if _map[y][x] != 0:
            for a in range(4):
                ny, nx = y + dy[a], x + dx[a]
                if in_range(ny, nx) and _map[ny][nx] == 0:

                    # 섬의 도착했을 때의 숫자를 세야 하므로 다리 길이는 0부터 시작
                    queue.append((ny, nx, 0, _map[y][x], dy[a], dx[a]))

# 3. BFS로 위에서 생성한 다리들을 완성시킨다. 이 때 길이가 1인 다리는 탈락시키고
# 중복을 방지하기 위해 숫자가 낮은 섬에서 높은 섬으로 가는 다리만 남긴다.

bridges = []  # (출발섬, 도착섬, 길이)

while queue:
    # (y, x, 다리 길이, 출발한 섬, 방향y, 방향x)
    y, x, bridge_len, island_start, *d = queue.popleft()

    if _map[y][x] != 0:  # 섬에 도착했다면

        # 길이가 1인 다리는 X, 출발섬이 도착섬보다 해시값이 낮아야 한다.
        if bridge_len == 1 or island_start >= _map[y][x]:
            continue

        bridges.append((island_start, _map[y][x], bridge_len))

    else:
        ny, nx = y + d[0], x + d[1]
        if in_range(ny, nx):
            queue.append((ny, nx, bridge_len + 1, island_start, *d))


##########################################################################
# 최소 신장 트리로 해결

# 섬의 번호는 2부터 시작
# graph[a] -> (비용, 도착섬)
graph = [[] for _ in range(island_cnt + 2)]
for a, b, c in bridges:
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [0] * (island_cnt + 2)
queue = [(0, 2)]  # 2부터 시작
ans = 0
cnt = 0

while queue:
    c, x = heapq.heappop(queue)
    if not visited[x]:
        visited[x] = 1
        ans += c
        cnt += 1
        for nc, nx in graph[x]:
            if not visited[nx]:
                heapq.heappush(queue, (nc, nx))


if cnt == island_cnt:
    print(ans)
else:
    print(-1)

##########################################################################
# 모든 경우를 탐색

ans = float("inf")
combies = []
visited = set()


# 4. DFS로 경우의 수를 탐색하면서 모든 섬을 연결하는 다리 길이의 최솟값을 구한다. 다리의 개수는 모든 섬의 개수 - 1 이다.
def dfs(i: int):
    if len(combies) == island_cnt - 1:
        global ans
        ans = min(ans, sum(map(lambda x: bridges[x][2], combies)))
        return

    for x in range(i, len(bridges)):
        island_start, island_end, _ = bridges[x]
        v = (island_start, island_end)
        if x not in combies and v not in visited:
            combies.append(x)
            visited.add(v)
            dfs(x)
            combies.pop()
            visited.remove(v)


dfs(0)


print(ans if ans != float("inf") else -1)
