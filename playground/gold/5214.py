# 환승

"""
같은 하이퍼튜브에 속하는 역들을 하나로 묶어서 공간 복잡도 최소화

다만 시간복잡도는 다소 늘어남
"""

import sys
from collections import deque

input = sys.stdin.readline

N, K, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # graph[n] - n이 속해있는 하이퍼튜브 번호
hypertube = []

for _ in range(M):
    h = list(map(int, input().split()))
    hn = len(hypertube)
    for n in h:
        graph[n].append(hn)

    hypertube.append(h)


q = deque()
q.append((1, 1))  # time, node

visit = [0] * (N + 1)
visit[1] = 1

while q:
    t, n = q.popleft()
    if n == N:
        print(t)
        exit(0)

    for hn in graph[n]:
        for nn in hypertube[hn]:
            if nn != n and not visit[nn]:
                visit[nn] = 1
                q.append((t + 1, nn))

print(-1)
