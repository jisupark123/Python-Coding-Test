# 팀배분

"""
적대 관계에 있는 사람들을 각각 다른 색(1, -1)으로 색칠하기
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    for x in list(map(int, input().split()))[1:]:
        graph[i].append(x)
        graph[x].append(i)

colors = [0] * (N + 1)

for i in range(1, N + 1):
    if colors[i] == 0:
        dq = deque()

        dq.append(i)
        colors[i] = 1

        while dq:
            x = dq.popleft()
            for nx in graph[x]:
                if colors[nx] == 0:
                    colors[nx] = colors[x] * -1
                    dq.append(nx)

team1 = [i for i in range(N + 1) if colors[i] == 1]
team2 = [i for i in range(N + 1) if colors[i] == -1]

print(len(team1))
print(*team1)
print(len(team2))
print(*team2)
