# 바둑

# 바둑판[r][c]에 돌을 놓는 경우와 안놓는 경우가 존재
# 만약 돌을 놓는 경우 이미 돌의 개수를 초과했는지 검사한다. (검사하면서 이미 바둑판이 완성되었는지 체크)
# 돌을 놓지 않은 경우는 검사할 필요 X
# 바둑판을 순회하면서 모든 경우를 조사한다.
# 가능한 경우가 나오면 True 반환 -> 함수 종료

import sys

input = sys.stdin.readline

N = int(input())

# list[i] -> i 행에 놓인 돌의 개수
row_counts = list(map(int, input().split()))

# list[i] -> i 열에 놓인 돌의 개수
col_counts = list(map(int, input().split()))

# list[i] -> 왼쪽 위부터 i번째 대각선에 놓인 돌의 개수
left_top_diagonal_counts = list(map(int, input().split()))

# list[i] -> 왼쪽 아래부터 i번째 대각선에 놓인 돌의 개수
left_bottom_diagonal_counts = list(map(int, input().split()))

# N x N 바둑판
board = [[-1 for _ in range(N)] for _ in range(N)]


def possible():
    pass


def make_board():
    for r in range(N):
        for c in range(N):
            if board[r][c] == -1:
                board[r][c] = 1
                if possible():
                    make_board()
