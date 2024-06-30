# 백조의 호수

"""
union-find

1. 백조 위치 저장 후 물로 변환
2. 연결되어 있는 물 좌표끼리 union 
3. 녹을 지점 melt에 저장 (2,3번 동시에 진행)
3. 하루가 지날 때마다 다음을 수행
- melt의 좌표를 꺼냄
- 녹을 지점(i,j)을 물로 변환
- (i,j)의 인접 좌표에 물(.)이 있다면 union
- (i,j)의 인접 좌표에 빙하(X)가 있다면 next_melt에 따로 저장
- melt에서 좌표를 모두 꺼낸 후 melt <- next_melt로 교체
- 두 백조가 같은 집합이라면 반복문 종료

"""

import sys
from collections import deque


# sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def in_range(i, j):
    return 0 <= i < r and 0 <= j < c


def find(i, j):
    if parents[i][j] == (i, j):
        return (i, j)
    parents[i][j] = find(*parents[i][j])
    return parents[i][j]


def union(a, b):
    i, j = find(*a)
    k, l = find(*b)

    if ranks[i][j] > ranks[k][l]:
        parents[k][l] = (i, j)
    elif ranks[i][j] < ranks[k][l]:
        parents[i][j] = (k, l)
    else:
        parents[k][l] = (i, j)
        ranks[i][j] += 1


r, c = map(int, input().split())


lake = [list(input().strip()) for _ in range(r)]
parents = [[(i, j) for j in range(c)] for i in range(r)]
ranks = [[0] * c for _ in range(r)]
visit = [[0] * c for _ in range(r)]
swans = []  # 백조 좌표

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for i in range(r):
    for j in range(c):
        if lake[i][j] == "L":
            swans.append((i, j))
            lake[i][j] = "."
            if len(swans) == 2:
                break


melt = []  # 녹을 곳
for i in range(r):
    for j in range(c):

        if not visit[i][j] and lake[i][j] == ".":

            queue = deque()
            queue.append((i, j))
            visit[i][j] = 1

            while queue:
                y, x = queue.popleft()
                parents[y][x] = (i, j)  # union
                for a in range(4):
                    ny, nx = y + dy[a], x + dx[a]
                    if in_range(ny, nx) and not visit[ny][nx]:
                        visit[ny][nx] = 1
                        if lake[ny][nx] == ".":
                            queue.append((ny, nx))
                        else:
                            melt.append((ny, nx))


day = 0

while find(*swans[0]) != find(*swans[1]):
    next_melt = []

    for i, j in melt:
        lake[i][j] = "."
        for a in range(4):
            ni, nj = i + dy[a], j + dx[a]
            if in_range(ni, nj):
                if not visit[ni][nj] and lake[ni][nj] == "X":
                    visit[ni][nj] = 1
                    next_melt.append((ni, nj))

                elif lake[ni][nj] == ".":
                    union((i, j), (ni, nj))

    melt = next_melt

    day += 1

print(day)
