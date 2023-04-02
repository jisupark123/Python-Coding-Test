# 미로만들기

import sys
import heapq

input = sys.stdin.readline
N = int(input())

maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

"""
미로를 탐색할 큐를 생성
"""

queue = [[0, 0, 0]]
distance = [[-1 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

while queue:
    cost, r, c = heapq.heappop(queue)
    if r == N - 1 and c == N - 1:
        print(cost)
        exit(0)

    for d in direction:
        next_r = r + d[0]
        next_c = c + d[1]
        if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
            next_cost = 0 if maze[next_r][next_c] == 1 else 1
            visited[next_r][next_c] = True
            heapq.heappush(queue, [cost + next_cost, next_r, next_c])
