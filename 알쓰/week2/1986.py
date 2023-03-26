# 체스

import sys


def mark_piece():
    for i in range(0, len(queen_pos), 2):
        board[queen_pos[i]][queen_pos[i + 1]] = 2
    for i in range(0, len(knight_pos), 2):
        board[knight_pos[i]][knight_pos[i + 1]] = 2
    for i in range(0, len(pawn_pos), 2):
        board[pawn_pos[i]][pawn_pos[i + 1]] = 2


def mark_move():
    for i in range(0, len(queen_pos), 2):
        queen_y = queen_pos[i]
        queen_x = queen_pos[i + 1]
        for y, x in queen_move:
            next_y = queen_y + y
            next_x = queen_x + x
            while True:
                if 0 <= next_y < n and 0 <= next_x < m and board[next_y][next_x] != 2:
                    board[next_y][next_x] = 1
                    next_y += y
                    next_x += x
                else:
                    break

    for i in range(0, len(knight_pos), 2):
        knight_y = knight_pos[i]
        knight_x = knight_pos[i + 1]
        for y, x in knight_move:
            next_y = knight_y + y
            next_x = knight_x + x
            if 0 <= next_y < n and 0 <= next_x < m and board[next_y][next_x] != 2:
                board[next_y][next_x] = 1


input = sys.stdin.readline
n, m = map(int, input().split())

# 0 -> 안전한 칸
# 1 -> 안전하지 않은 칸
# 2 -> 체스말
board = [[0 for _ in range(m)] for _ in range(n)]

queen_pos = list(map(lambda x: int(x) - 1, input().split()))[1:]
knight_pos = list(map(lambda x: int(x) - 1, input().split()))[1:]
pawn_pos = list(map(lambda x: int(x) - 1, input().split()))[1:]

# 각 체스말의 이동 범위 (x,y)
queen_move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
knight_move = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

mark_piece()
mark_move()

res = 0

for i in range(n):
    res += board[i].count(0)


print(res)
