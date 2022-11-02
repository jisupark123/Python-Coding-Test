# 오목

from sys import stdin


input = stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]
direction = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, -1], [1, 1], [-1, -1], [-1, 1]]


def can_win(row, col) -> list or False:
    dol = board[row][col]  # black or white
    for d in direction:
        r = row
        c = col
        is_five = False
        for i in range(2, 6):
            try:
                r += d[0]
                c += d[1]
                if board[r][c] != dol:
                    break
                if i == 5:
                    is_five = True
                    break
            except:
                break
        if is_five:
            if (
                0 <= r + d[0] < 19
                and 0 <= c + d[1] < 19
                and board[r + d[0]][c + d[1]] != dol
                and board[row + (d[0] * -1)][col + (d[1] * -1)] != dol
            ):
                res = []
                d = list(map(lambda x: x * -1, d))
                for _ in range(5):
                    res.append([r, c])
                    r += d[0]
                    c += d[1]
                return res
    return False


def get_res():
    for r in range(19):
        for c in range(19):
            if board[r][c] != 0:
                res = can_win(r, c)
                if res:
                    res.sort(key=lambda x: (x[0], x[1]))
                    print(board[r][c])
                    print(res[0][0] + 1, res[0][1] + 1)
                    return
    print(0)
    return


get_res()
