# 중량제한

"""
f(x) -> a에서 b까지 최대 중량 x로 이동할 수 있나 

x의 최댓값을 이분 탐색으로 search
"""

import sys
from collections import deque

input = sys.stdin.readline


def possible(x):

    colors = [-1] * (N + 1)  # 같은 집합끼리 같은 색으로
    colors[a] = 0
    colors[b] = 1
    queue = deque([a, b])

    while queue:

        node = queue.popleft()
        for nn, cost in graph[node]:

            if cost >= x:  # 중량 제한에 걸리지 않는다면

                if colors[nn] == -1:  # 안가본 곳이면 탐색
                    colors[nn] = colors[node]
                    queue.append(nn)

                elif colors[nn] != colors[node]:  # 다른 집합이면 a와 b 통행 가능
                    return True

    return False


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

a, b = map(int, input().split())

start = 1
end = 1000000000
ans = 0

while start <= end:
    mid = (start + end) // 2

    if possible(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
