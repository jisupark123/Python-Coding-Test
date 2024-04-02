# 적의 적

# 이분그래프인지 판별

import sys
from collections import deque

input = sys.stdin.readline

RED = 1
BLACK = 2

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

colors = [0] * (N + 1)  # 0 - 색칠 안됨

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def is_bipartite_graph():
    for i in range(1, N + 1):
        if colors[i] == 0:
            queue = deque()

            queue.append((i, RED))  # node, color
            colors[i] = RED

            while queue:
                n, c = queue.popleft()

                for nn in graph[n]:
                    nc = RED if c == BLACK else BLACK

                    if colors[nn] == 0:
                        colors[nn] = nc
                        queue.append((nn, nc))

                    # 색칠하려는 노드가, 칠하려는 색과 다른 색으로 칠해져 있다면
                    elif colors[nn] != nc:
                        return False

    return True


print(1 if is_bipartite_graph() else 0)
