# LCA

"""
1. 트리 구성 시 모든 노드의 depth를 구한다.
2. 구하려는 두 노드의 depth를 맞춰주기 위해, 더 깊은 depth를 가진 노드의 포인터를 그 차이만큼 부모로 이동시킨다.
3. 두 노드의 포인터를 하나씩 올리면서 같은 포인터로 만날 때까지 반복
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]  # graph[x] -> x와 연결된 노드들
parent = [0] * (N + 1)  # parent[x] -> x의 부모
d = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# bfs로 1번 노드부터 트리 구성

q = deque()
q.append((-1, 1, 0))  # (부모, 자식, depth)

while q:
    p, x, depth = q.popleft()
    parent[x] = p
    d[x] = depth

    for nx in graph[x]:
        if nx != p:
            q.append((x, nx, depth + 1))


M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    while d[a] != d[b]:
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]

    print(a)
