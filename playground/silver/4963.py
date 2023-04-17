# 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline

direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
res = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    lst = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    visit = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if lst[i][j] == 1 and not visit[i][j]:
                queue = deque()
                queue.append((i, j))
                while queue:
                    r, c = queue.popleft()
                    for d in direction:
                        next_r = r + d[0]
                        next_c = c + d[1]
                        if (
                            0 <= next_r < h
                            and 0 <= next_c < w
                            and lst[next_r][next_c] == 1
                            and not visit[next_r][next_c]
                        ):
                            visit[next_r][next_c] = True
                            queue.append((next_r, next_c))

                cnt += 1

    res.append(cnt)

for r in res:
    print(r)
