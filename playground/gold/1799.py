# 비숍

"""
처음부터 말을 놓을 수 없는 곳은 무한대의 값을 넣어줌
말을 놓을 board를 따로 관리함

후보지에 말을 하나씩 추가하는 경우의 수를 탐색

말을 추가할 때는 갈 수 있는 경로에 모두 1씩 더해준다. (해당 말을 놓는 칸은 그대로 놔둠)
만약 말이 있는 모든 칸이 모두 0이라면 -> 가능한 경우

최적화
- 남은 곳을 다 채워도 이미 구한 답보다 같거나 작다면 중단

"""

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

# board = [list(map(int, input().split())) for _ in range(N)]
board = [[1] * N for _ in range(N)]

candidates = []  # 비숍을 놓을 수 있는 곳들 (후보지)

# 비숍을 놓을 수 없는 곳에는 inf, 비숍을 놓을 수 있는 곳에는 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            candidates.append((i, j))
            board[i][j] = 0
        elif board[i][j] == 0:
            board[i][j] = float("inf")


# 비숍의 위치를 저장할 리스트
# 비숍 -> 1, 빈 곳 -> 0
sim_board = [[0] * N for _ in range(N)]


# 말이 갈 수 있는 곳을 return (말이 놓인 곳 제외)
def markable(r, c):
    lst = []

    # 왼쪽 위부터 오른쪽 아래까지
    nr = r - min(r, c)
    nc = c - min(r, c)
    for _ in range(N - max(nr, nc)):
        lst.append((nr, nc))
        nr += 1
        nc += 1

    # 왼쪽 아래부터 오른쪽 위까지
    nr = r + min(N - 1 - r, c)
    nc = c - min(N - 1 - r, c)
    for _ in range(N - max(N - 1 - nr, nc)):
        lst.append((nr, nc))
        nr -= 1
        nc += 1

    return lst


# r,c 자리에 놓을 수 있는지
def is_legal(r, c):
    if board[r][c] != 0:  # 이미 마킹되어있는 곳
        return False

    for nr, nc in markable_caching[r][c]:
        if sim_board[nr][nc] == 1:
            return False

    return True


# 갈 수 있는 곳을 마킹
def mark(r, c):
    global blank_cnt
    for nr, nc in markable_caching[r][c]:
        if board[nr][nc] == 0:  # 빈곳이라면
            blank_cnt -= 1
        board[nr][nc] += 1
    board[r][c] = 1


# 갈 수 있는 곳을 언마킹
def unmark(r, c):
    global blank_cnt
    for nr, nc in markable_caching[r][c]:
        board[nr][nc] -= 1
        if board[nr][nc] == 0:  # 빈곳이라면
            blank_cnt += 1
    board[r][c] = 0


# 각 칸마다 비숍이 갈 수 있는 곳을 저장해놓기
markable_caching = [[markable(r, c) for c in range(N)] for r in range(N)]

# 말을 하나씩 추가하면서 모든 조합을 탐색
# 가능한 경우가 나오면 추가한 말의 개수를 res에 저장

res = 0
visited = []  # 비숍을 놓은 곳들
simulation = []
blank_cnt = len(candidates)  # 말을 놓을 수 있는 곳 개수
n = 0  # 놓인 말의 개수


def dfs(idx):
    global n, res
    if n + blank_cnt <= res:  # 남은 곳을 다 채워도 이미 구한 답보다 같거나 작다면 중단
        return
    for i in range(idx, len(candidates)):
        if i in visited:
            continue
        r, c = candidates[i]
        legal = is_legal(r, c)
        if legal:  # 말을 놓는 것이 가능하다면
            n += 1
            sim_board[r][c] = 1
            mark(r, c)
            res = max(res, n)

        visited.append(i)
        dfs(i)
        visited.pop()

        if legal:
            unmark(r, c)
            n -= 1
            sim_board[r][c] = 0


dfs(0)
print(res)
