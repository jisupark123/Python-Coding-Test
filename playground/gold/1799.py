# 비숍
# 8개 경우의 수는 7개 경우의 수를 바탕으로 진행

import sys

input = sys.stdin.readline

N = int(input())

#  비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]


candidates = []  # 비숍을 놓을 수 있는 곳들
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            candidates.append((i, j))

BISHOP = 2


# r,c 자리에 놓을 수 있는지
def is_legal(r, c):
    if board[r][c] != 1:
        return False
    # 왼쪽 위부터 오른쪽 아래까지 대각선 검사
    nr = r - min(r, c)
    nc = c - min(r, c)
    for _ in range(N - max(nr, nc)):
        if board[nr][nc] == BISHOP:
            return False
        nr += 1
        nc += 1

    # 왼쪽 아래부터 오른쪽 위까지 대각선 검사
    nr = r + min(N - 1 - r, c)
    nc = c - min(N - 1 - r, c)
    for _ in range(N - max(N - 1 - nr, nc)):
        if board[nr][nc] == BISHOP:
            return False
        nr -= 1
        nc += 1

    return True


# r개의 비숍을 놓는 것이 가능한지
def possible(r):
    visited = [0] * len(candidates)
    p = False

    def dfs(depth, idx):
        nonlocal p
        # depth가 r과 같아지면 성공
        if p or depth == r:
            # print([candidates[x] for x in range(len(candidates)) if visited[x] == 1])
            p = True
            return
        for i in range(idx, len(candidates)):
            if p:
                return
            row, col = candidates[i]
            if not visited[i] and is_legal(row, col):
                visited[i] = 1
                board[row][col] = BISHOP
                dfs(depth + 1, i)
                board[row][col] = 1
                visited[i] = 0

    dfs(0, 0)

    return p


start = 1
end = len(candidates)

ans = 1

while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
