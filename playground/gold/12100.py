# 2048 (Easy)

import sys

input = sys.stdin.readline


def add_undo():
    lst = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                lst.append((i, j, board[i][j]))

    undo_stack.append(lst)


# 입력한 방향에 따라 블록들을 움직이는 함수
# ex) 왼쪽
# 상태변수 p <- True (블록을 합칠 수 있는지) (연속으로 합칠 수 없음)
# 맨 왼쪽의 블록을 보드의 왼쪽 끝으로 이동시킨다.
# 1. 다음 블록이 맨 왼쪽의 블록과 숫자가 같고 p가 True라면 두 개의 블록을 합친다. && p <- False
# 2. 다음 블록이 맨 왼쪽의 블록과 숫자가 다르거나 p가 False라면 블록을 맨 왼쪽의 블록 오른쪽에 위치시킨다. && p <- True
def move(direction):
    if direction == "left":
        for i in range(N):
            # 맨 왼쪽의 블록을 보드의 왼쪽 끝으로 이동시킨다.
            for j in range(N):
                if board[i][j] != 0:
                    temp = board[i][j]
                    board[i][j] = 0
                    board[i][0] = temp
                    break

            prev = 0  # 이미 밀린 블록 중 가장 가까운 블록
            p = True  # 블록을 합칠 수 있는지 (연속으로 합칠 수 없음)

            for j in range(1, N):
                if board[i][j] != 0:
                    if board[i][j] == board[i][prev] and p:
                        board[i][prev] *= 2
                        board[i][j] = 0
                        p = False
                    else:
                        temp = board[i][j]
                        board[i][j] = 0
                        board[i][prev + 1] = temp
                        prev += 1
                        p = True
    if direction == "right":
        for i in range(N - 1, -1, -1):
            # 맨 오른쪽의 블록을 보드의 오른쪽 끝으로 이동시킨다.
            for j in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    temp = board[i][j]
                    board[i][j] = 0
                    board[i][N - 1] = temp
                    break

            prev = N - 1  # 이미 밀린 블록 중 가장 가까운 블록
            p = True  # 블록을 합칠 수 있는지 (연속으로 합칠 수 없음)

            for j in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    if board[i][j] == board[i][prev] and p:
                        board[i][prev] *= 2
                        board[i][j] = 0
                        p = False
                    else:
                        temp = board[i][j]
                        board[i][j] = 0
                        board[i][prev - 1] = temp
                        prev -= 1
                        p = True
    if direction == "bottom":
        for j in range(N):
            # 맨 아래의 블록을 보드의 아래 끝으로 이동시킨다.
            for i in range(N - 1, -1, -1):
                if board[i][j] != 0:
                    temp = board[i][j]
                    board[i][j] = 0
                    board[N - 1][j] = temp
                    break

            prev = N - 1  # 이미 밀린 블록 중 가장 가까운 블록
            p = True  # 블록을 합칠 수 있는지 (연속으로 합칠 수 없음)

            for i in range(N - 2, -1, -1):
                if board[i][j] != 0:
                    if board[i][j] == board[prev][j] and p:
                        board[prev][j] *= 2
                        board[i][j] = 0
                        p = False
                    else:
                        temp = board[i][j]
                        board[i][j] = 0
                        board[prev - 1][j] = temp
                        prev -= 1
                        p = True
    if direction == "top":
        for j in range(N):
            # 맨 위의 블록을 보드의 위 끝으로 이동시킨다.
            for i in range(N):
                if board[i][j] != 0:
                    temp = board[i][j]
                    board[i][j] = 0
                    board[0][j] = temp
                    break

            prev = 0  # 이미 밀린 블록 중 가장 가까운 블록
            p = True  # 블록을 합칠 수 있는지 (연속으로 합칠 수 없음)

            for i in range(1, N):
                if board[i][j] != 0:
                    if board[i][j] == board[prev][j] and p:
                        board[prev][j] *= 2
                        board[i][j] = 0
                        p = False
                    else:
                        temp = board[i][j]
                        board[i][j] = 0
                        board[prev + 1][j] = temp
                        prev += 1
                        p = True


N = int(input())

undo_stack = []  # [(i,j,숫자)]

board = [list(map(int, input().split())) for _ in range(N)]

# ← ↑ → ↓
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
directions = ["left", "right", "bottom", "top"]

res = 0


def dfs(n, direction):
    global board
    if n == 5:
        global res
        for i in range(N):
            for j in range(N):
                res = max(res, board[i][j])
        return
    copy = [[board[x][y] for y in range(N)] for x in range(N)]
    move(direction)
    for d in directions:
        dfs(n + 1, d)
    board = [[copy[x][y] for y in range(N)] for x in range(N)]


for d in directions:
    dfs(0, d)
print(res)
