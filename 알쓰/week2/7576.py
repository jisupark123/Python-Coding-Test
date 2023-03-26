# 토마토


def bfs():

    while len(queue) != 0:
        i, j = queue.popleft()
        for d in directions:
            if (
                # 가로 인덱스 검사
                0 <= i + d[0] < n
                # 세로 인덱스 검사
                and 0 <= j + d[1] < m
                # 한번도 방문하지 않았거나 전에 방문했을 때보다 더 효율적인 경로라면
                and (
                    box[i + d[0]][j + d[1]] == 0
                    or box[i + d[0]][j + d[1]] > box[i][j] + 1
                )
            ):
                box[i + d[0]][j + d[1]] = box[i][j] + 1
                queue.append([i + d[0], j + d[1]])


from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
bfs()
# for b in box:
#     print(b)


def get_res():
    res = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return -1
            res = max(res, box[i][j])
    return res - 1


print(get_res())
