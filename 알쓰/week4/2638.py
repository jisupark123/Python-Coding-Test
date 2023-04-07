# 치즈

"""

1. 종이 맵 생성
2. 치즈 위치 리스트에 저장
3. 바깥 공기 모두 숫자 2로 변경
4. 큐의 맨 왼쪽부터 치즈 꺼내서 녹는지 검사 (바깥 공기와 2변 이상 접촉)
5. 녹는 치즈는 melting 리스트에, 아닌 치즈는 다시 큐에 넣기
6. melting 리스트를 순회하면서, 녹는 치즈를 2(바깥 공기)로 변경
7. 동시에 녹는 치즈의 상하좌우 중에 0(안쪽 공기)가 있다면 인접한 안쪽 공기 모두 2(바깥 공기)로 변경 bfs
8. 결과에 1 추가하고 4번으로 이동 (큐가 끝날 때까지 계속)

"""

import sys
from collections import deque

input = sys.stdin.readline

CHEESE = 1
OUTER_AIR = 2
INNER_AIR = 0


def is_melting(i, j):
    cnt = 0
    for d in direction:
        if paper[i + d[0]][j + d[1]] == OUTER_AIR:
            cnt += 1
    if cnt >= 2:
        return True
    return False


def change_inner_air_to_outer_air(y, x):
    queue = deque()
    queue.append([y, x])
    while queue:
        i, j = queue.popleft()
        if paper[i][j] != INNER_AIR:
            continue
        paper[i][j] = OUTER_AIR
        for d in direction:
            ny, nx = i + d[0], j + d[1]
            if paper[ny][nx] == INNER_AIR:
                queue.append([ny, nx])


N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]
cheeses = deque()

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]


# 치즈 위치 찾기
for i in range(N):
    for j in range(M):
        if paper[i][j] == CHEESE:
            cheeses.append((i, j))

# 둘러쌓인 곳 찾기
# 처음에 바깥의 공기 모두 2로 변경
queue = deque()
queue.append([0, 0])
while queue:
    i, j = queue.popleft()
    if paper[i][j] != 0:
        continue
    paper[i][j] = OUTER_AIR
    for d in direction:
        next_i, next_j = i + d[0], j + d[1]
        if 0 <= next_i < N and 0 <= next_j < M and paper[next_i][next_j] == 0:
            queue.append([next_i, next_j])


res = 0

while cheeses:
    melting = []
    for _ in range(len(cheeses)):
        cheese = cheeses.popleft()
        if is_melting(*cheese):
            melting.append(cheese)
        else:
            cheeses.append(cheese)
    for c in melting:
        paper[c[0]][c[1]] = OUTER_AIR
        for d in direction:
            ny, nx = c[0] + d[0], c[1] + d[1]
            if paper[ny][nx] == INNER_AIR:
                change_inner_air_to_outer_air(ny, nx)

    res += 1


print(res)
