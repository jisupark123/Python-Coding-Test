import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())


_map = [list(map(int, input().split())) for _ in range(N)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

in_range = lambda y, x: 0 <= y < N and 0 <= x < M

# visited[y][x][gram] -> y, x, gram 에서의 최소 이동 시간
visited = [[[float("inf")] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 0

queue = deque()
queue.append((0, 0, 0, False))  # y, x, 시간, 그람 보유 여부

ans = None

while queue:
    y, x, t, gram = queue.popleft()

    if y == N - 1 and x == M - 1:
        ans = t
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if in_range(ny, nx):

            if _map[ny][nx] == 1 and not gram:
                continue

            nt = t + 1
            ngram = gram or _map[ny][nx] == 2

            if nt <= T and visited[ny][nx][ngram] > nt:
                visited[ny][nx][ngram] = nt
                queue.append((ny, nx, nt, ngram))

if ans is None:
    print("Fail")
else:
    print(ans)
