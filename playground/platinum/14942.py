# 개미

"""
한 방에서 다른 방으로 갈 수 있는 경로는 항상 존재하며 유일하다 -> 사이클이 없는 트리 형태의 그래프

1. 1로 이동하려면 어느 노드로 이동해야 하는지 각 노드마다 구하기
2. bfs로 최종 도착지 구하기
"""

import sys
from collections import deque


input = sys.stdin.readline

N = int(input())


energy = [0] + [int(input()) for _ in range(N)]

graph = [[] for _ in range(N + 1)]


for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))


next_x = [0] * (N + 1)

q = deque()
q.append((1, -1))

while q:
    x, px = q.popleft()
    for cost, nx in graph[x]:
        if nx != px:
            q.append((nx, x))
            next_x[nx] = (x, cost)

# 현재 노드, 에너지, 시작 노드
q = deque([(x, energy[x], x) for x in range(1, N + 1)])

ans = [0] * (N + 1)

while q:
    x, e, start_x = q.popleft()
    if x == 1:
        ans[start_x] = 1
        continue

    nx, nc = next_x[x]
    if nc > e:
        ans[start_x] = x
    else:
        q.append((nx, e - nc, start_x))

for a in ans[1:]:
    print(a)
