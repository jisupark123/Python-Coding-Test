# 이분 그래프

"""
그래프의 임의의 지점에서 시작해서, Black과 Red를 칠한다.

이 때, 인접한 그래프는 서로 다른 색을 칠해야 한다.

만약 색칠하려는 노드가, 칠하려는 색과 다른 색으로 칠해져 있다면 이분 그래프가 아닌 것.

BFS로 구현
"""

import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

RED = 1
BLACK = 2

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V + 1)]

    colors = [0] * (V + 1)  # 0 - 색칠 안됨

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def is_bipartite_graph():
        for i in range(1, V + 1):
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

    print("YES" if is_bipartite_graph() else "NO")
