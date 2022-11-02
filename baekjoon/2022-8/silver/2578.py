# 빙고

from sys import stdin


input = stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
nums = sum([list(map(int, input().split())) for _ in range(5)], [])

count = 0


# 빙고가 몇개 있는지 체크하는 함수
# 가로 5개, 세로 5개, 왼쪽 대각선, 오른쪽 대각선 차례로 체크
def check():
    bingo = 0

    for i in range(5):  # 가로 체크
        flag = True
        for j in range(5):
            if board[i][j] != False:
                flag = False
                break
        if flag:
            bingo += 1

    for i in range(5):  # 세로 체크
        flag = True
        for j in range(5):
            if board[j][i] != False:
                flag = False
                break
        if flag:
            bingo += 1

    flag = True
    for i in range(5):  # 왼쪽 -> 오른쪽 대각선 체크
        if board[i][i] != False:
            flag = False
            break
    if flag:
        bingo += 1

    flag = True
    for i in range(5):  # 오른쪽 -> 왼쪽 대각선 체크
        if board[i][4 - i] != False:
            flag = False
            break
    if flag:
        bingo += 1

    return bingo


for num in nums:
    changed = False
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = False
                changed = True
                break
        if changed:
            break
    count += 1

    if changed and check() >= 3:
        print(count)
        break
