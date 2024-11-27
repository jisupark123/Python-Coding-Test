# 도미노

"""
그래프의 scc(strongly connected component)를 구하고 

indegree가 0인 scc 찾기 (하나의 scc가 다른 scc를 가리킬 수 있음)


"""


import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    reversed_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        reversed_graph[b].append(a)

    def dfs(x):
        visited[x] = 1
        for nx in graph[x]:
            if not visited[nx]:
                dfs(nx)
        stack.append(x)

    stack = []
    visited = [0] * (N + 1)

    for x in range(1, N + 1):
        if not visited[x]:
            dfs(x)

    def reversed_dfs(x):
        visited[x] = 1
        for nx in reversed_graph[x]:
            if not visited[nx]:
                reversed_dfs(nx)
        scc.append(x)

    visited = [0] * (N + 1)
    scc_map = {}
    _hash = 0

    for x in stack[::-1]:
        scc = []
        if not visited[x]:
            reversed_dfs(x)

            for s in scc:
                scc_map[s] = _hash

            _hash += 1

    indegree = [0] * _hash

    for x in range(1, N + 1):
        for nx in graph[x]:
            if scc_map[x] != scc_map[nx]:
                indegree[scc_map[nx]] += 1

    print(indegree.count(0))
