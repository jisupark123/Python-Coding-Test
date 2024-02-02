# 별자리 만들기

import sys
import heapq

input = sys.stdin.readline


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


N = int(input())

stars = [list(map(float, input().split())) for _ in range(N)]

visited = [0] * N
queue = [(0, 0)]  # 거리, 노드

ans = 0

while queue:
    d, n = heapq.heappop(queue)
    if not visited[n]:
        visited[n] = 1
        ans += d

        for nn in range(N):
            if not visited[nn]:
                nd = distance(stars[n], stars[nn])
                heapq.heappush(queue, (nd, nn))

print(ans)
