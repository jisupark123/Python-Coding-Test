# 새내기와 헌내기

"""
- 각 부분 그래프에 대해서 탐색
- 신고한 사실에 따라 이분 그래프를 탐색한다.
- 두 집합을 각각 관리하고 탐색이 끝났을 때 더 많이 나온 집합의 크기를 헌내기(결과)에 더한다.
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    tmp = list(map(int, list(input().strip())))
    for j in range(N):
        if tmp[j] == 1:
            graph[i].append(j)

ans = 0

visited = [0] * (N)  # 1 or -1

for i in range(N):
    if visited[i] == 0:
        visited[i] = 1

        dq = deque()
        dq.append(i)

        plus = 1
        minus = 0

        while dq:
            x = dq.popleft()
            for nx in graph[x]:
                if visited[nx] == 0:
                    visited[nx] = visited[x] * -1
                    if visited[nx] == 1:
                        plus += 1
                    else:
                        minus += 1

                    dq.append(nx)

        ans += max(plus, minus)

print(ans)
