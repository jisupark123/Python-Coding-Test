# 스도쿠
#
# 스도쿠를 돌면서 빈자리(0)를 탐색한다
# 빈자리에 1~9 를 넣었을 때 세로,가로,칸에 대해 각각 가능한지 테스트해보고
# 가능하다면 스도쿠판에 숫자를 넣고 재귀함수를 호출한다.
# 가능한 케이스가 발견되면 출력 후 프로그램을 종료한다 (exit(0))
# 재귀호출한 함수가 반환되면(실패하면) 숫자를 넣었던 자리에 0을 넣어서 다시 되돌린다.


import sys

input = sys.stdin.readline


# 같은 행에 중복되는 숫자가 없는지
def check_row(row, n):
    for i in range(9):
        if n == sudoku[row][i]:
            return False
    return True


# 같은 열에 중복되는 숫자가 없는지
def check_col(col, n):
    for i in range(9):
        if n == sudoku[i][col]:
            return False
    return True


# 같은 칸에 중복되는 숫자가 없는지
def check_rect(row, col, n):
    # 각 칸이 시작하는 인덱스를 구함
    # 012 345 678
    # 2 -> 0
    # 5 -> 3
    real_row = row // 3 * 3
    real_col = col // 3 * 3
    for y in range(3):
        for x in range(3):
            if n == sudoku[real_row + y][real_col + x]:
                return False
    return True


sudoku = [[] for _ in range(9)]  # 스도쿠 판
empty_place = []  # 빈자리[(row,col)]

# 스도쿠판에 숫자 채우기 & 빈자리는 따로 리스트에 보관
for n in range(9):
    for m, num in enumerate([int(x) for x in input().split()]):
        sudoku[n].append(num)
        if num == 0:
            empty_place.append((n, m))


def dfs(n):
    if n == len(empty_place):
        for i in range(9):
            print(*sudoku[i])
        exit(0)
    row = empty_place[n][0]
    col = empty_place[n][1]
    for i in range(1, 10):
        if check_row(row, i) and check_col(col, i) and check_rect(row, col, i):
            sudoku[row][col] = i  # 1~9 숫자 넣고
            dfs(n + 1)  # 새로운 분기 시작
            sudoku[row][col] = 0  # 분기가 종료되면 (답이 없다면) 원상태 복구


dfs(0)
