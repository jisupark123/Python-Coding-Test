# 벽 부수고 이동하기

"""
기존의 bfs 구현방식에 벽을 뚫는 것이 추가된 문제
원래의 이차원 visit 테이블에 차원 하나를 추가해서 벽을 뚫은 횟수 로직을 추가한다.
"""


import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

_map = [list(map(int, list(input().strip()))) for _ in range(N)]


queue = deque()
queue.append([0, 0, 1, 1])  # i, j, cost, 벽 부수기 남은 횟수

# visit[7][8][0] -> 7행 8열 방문 & 벽을 이미 부순 상태
visit = [[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

while queue:
    i, j, cost, wall_cnt = queue.popleft()
    if i == N - 1 and j == M - 1:
        print(cost)
        exit(0)
    for d in direction:
        next_i = i + d[0]
        next_j = j + d[1]
        if 0 <= next_i < N and 0 <= next_j < M and not visit[next_i][next_j][wall_cnt]:
            if _map[next_i][next_j] == 1:
                if wall_cnt == 1:
                    visit[next_i][next_j][wall_cnt] = True
                    queue.append([next_i, next_j, cost + 1, 0])
                else:
                    continue

            else:
                visit[next_i][next_j][wall_cnt] = True
                queue.append([next_i, next_j, cost + 1, wall_cnt])


print(-1)
