# 트리

"""
- 각각의 노드는 하나의 집합
- dfs와 Union 연산을 통해서 집합들을 합친다.
- dfs 도중 탐색하는(연결된) 노드의 대표 노드가 해당 집합의 노드와 같다면 사이클 발생 -> 대표 노드를 cycle set에 추가
- dfs 탐색 도중 방문했던 노드에 다시 방문하면 사이클 발생하는 것
- 탐색한 노드를 다음 dfs에서 탐색하면 안되므로 방문 처리 필요
- 부모 노드 배열에 있는 '유니크한 대표 노드 개수'와 cycle set의 차집합의 개수를 출력
"""

import sys

input = sys.stdin.readline

i = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # x의 대표 노드
    def find(x):
        if parents[x] == x:
            return x

        return find(parents[x])

    # a와 b 합치기
    def union(a, b):
        parents[find(b)] = find(a)

    parents = [x for x in range(n + 1)]  # parents[x] -> graph[x]의 부모 노드

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    cycle = set()

    visited = [0] * (n + 1)

    def dfs(x, parent):
        visited[x] = 1
        for nx in graph[x]:
            if nx != parent:
                if find(x) == find(nx):  # 사이클 발생
                    cycle.add(find(x))
                else:
                    union(x, nx)
                    dfs(nx, x)

    for x in range(1, n + 1):
        if not visited[x]:
            dfs(x, -1)

    unique = set([find(x) for x in parents[1:]])

    tree_cnt = len(unique - cycle)

    if tree_cnt == 0:
        print(f"Case {i}: No trees.")
    elif tree_cnt == 1:
        print(f"Case {i}: There is one tree.")
    else:
        print(f"Case {i}: A forest of {tree_cnt} trees.")

    i += 1
