# 미로만들기

import sys
import heapq

input = sys.stdin.readline
N = int(input())

# 미로 생성
maze = [list(map(int, list(input().rstrip()))) for _ in range(N)]

# 미로를 탐색할 큐를 생성
queue = [[0, 0, 0]]

# 방문처리할 리스트 NxN
visited = [[False for _ in range(N)] for _ in range(N)]

# 상하좌우 4방향
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

while queue:
    cost, r, c = heapq.heappop(queue)

    # 도착지면 출력 후 프로그램 종료
    if r == N - 1 and c == N - 1:
        print(cost)
        exit(0)

    # 상하좌우 4방향 탐색 (인덱스 초과, 방문 했는지 검사)
    for d in direction:
        next_r = r + d[0]
        next_c = c + d[1]
        if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
            # 흰 방, 검은 방 종류에 따라 가중치 0 or 1로 설정
            next_cost = 0 if maze[next_r][next_c] == 1 else 1
            visited[next_r][next_c] = True
            heapq.heappush(queue, [cost + next_cost, next_r, next_c])
