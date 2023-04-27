# 토마토


import sys
from collections import deque

input = sys.stdin.readline

RIPEN = 1
NOT_RIPEN = 0
EMPTY = -1

M, N, H = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 6방향
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

queue = deque()  # (h,n,m,시간)
visit = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]

for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == RIPEN:
                queue.append((h, n, m, 0))

day_cnt = 0
while queue:
    h, n, m, day = queue.popleft()
    day_cnt = max(day_cnt, day)
    for d in direction:
        if (
            0 <= h + d[0] < H
            and 0 <= n + d[1] < N
            and 0 <= m + d[2] < M
            and not visit[h + d[0]][n + d[1]][m + d[2]]
            and box[h + d[0]][n + d[1]][m + d[2]] == NOT_RIPEN
        ):
            box[h + d[0]][n + d[1]][m + d[2]] = RIPEN
            visit[h + d[0]][n + d[1]][m + d[2]] = True
            queue.append((h + d[0], n + d[1], m + d[2], day + 1))

for a in box:
    for b in a:
        for c in b:
            if c == NOT_RIPEN:
                print(-1)
                exit(0)

print(day_cnt)
