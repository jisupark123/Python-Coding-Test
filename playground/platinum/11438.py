# LCA 2

"""
기존 LCA 해결 방법
1. 트리 구성 시 모든 노드의 depth를 구한다.
2. 구하려는 두 노드의 depth를 맞춰주기 위해, 더 깊은 depth를 가진 노드의 포인터를 그 차이만큼 부모로 이동시킨다.
3. 두 노드의 포인터를 하나씩 올리면서 같은 포인터로 만날 때까지 반복

LCA(2)는 구하는 노드의 쌍이 10000 -> 100000으로 많아졌고 시간도 3초 -> 1초로 줄었기 때문에 최적화시키는 과정이 필요하다.

1. 노드마다 일정한 간격의 조상 노드를 미리 구해놓는다. (log2(노드 개수))
2. 포인터를 이동시킬 때 하나씩 이동시키지 말고 위의 간격마다 이동시킨다. (이때 비트마스킹 이용하면 편리)
"""

import sys
from collections import deque
from math import log2

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]  # graph[x] -> x와 연결된 노드들
parent = [0] * (N + 1)  # parent[x] -> x의 부모
depth = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# bfs로 1번 노드부터 트리 구성

q = deque()
q.append((-1, 1, 0))  # (부모, 자식, depth)

while q:
    p, x, d = q.popleft()
    parent[x] = p
    depth[x] = d

    for nx in graph[x]:
        if nx != p:
            q.append((x, nx, d + 1))

# dp[i][j] -> i에서 2**j번째 조상 노드
logn = int(log2(N) + 1)
dp = [[-1] * logn for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = parent[i]

# 2**j = 2**(j-1) * 2**(j-1) -> i의 2**j번째 조상 = i의 2**(j-1)번째 조상의 2**(j-1)번째 조상
# dp[i][j] = dp[dp[i][j-1]][j-1]


for j in range(1, logn):
    for i in range(1, N + 1):
        if dp[i][j - 1] != -1:
            dp[i][j] = dp[dp[i][j - 1]][j - 1]


M = int(input())

for _ in range(M):
    a, b = map(int, input().split())

    if depth[a] > depth[b]:
        a, b = b, a
    diff = depth[b] - depth[a]

    # depth 맞춰주기
    for i in range(logn):
        if diff & (1 << i):
            b = dp[b][i]

    if a == b:
        print(a)
        continue

    for i in range(logn - 1, -1, -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]

    print(dp[a][0])
