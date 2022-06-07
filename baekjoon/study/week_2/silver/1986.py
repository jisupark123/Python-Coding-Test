# 체스
import sys

input = sys.stdin.readline
h, w = map(int, input().split())

# 체스판 생성
board = [[False for _ in range(w)] for _ in range(h)]

# 각 체스말의 포지션 input 받기
def recieve_pos():
    array = list(map(lambda x: int(x) - 1, input().split()))
    return [array[i : i + 2] for i in range(1, len(array), 2)]


# 체스말 배치
def place_piece(piece, pos):
    global board
    for p in pos:
        board[p[0]][p[1]] = piece


# 체스판 확인
def view_board(lst):
    for l in lst:
        print(l)


# Queen, Knight의 사정거리 안에 있으면 0으로 변환
def mark_zero(pos, move):
    global board
    for p in pos:
        for m in move:
            original_pos = p
            while True:
                try:
                    next_pos = [x + y for x, y in zip(original_pos, m)]
                    if (
                        board[next_pos[0]][next_pos[1]] in [False, "X"]
                        and next_pos[0] >= 0
                        and next_pos[1] >= 0
                    ):
                        board[next_pos[0]][next_pos[1]] = "X"
                        original_pos = next_pos
                    else:
                        break
                except:
                    break


def count_element_in_double_list(element, list):
    res = 0
    for i in list:
        for j in i:
            if j == element:
                res += 1
    return res


# 각 체스말의 포지션 input 받기
queen_pos = recieve_pos()
knight_pos = recieve_pos()
pawn_pos = recieve_pos()

# 체스말 배치
place_piece("Q", queen_pos)
place_piece("K", knight_pos)
place_piece("P", pawn_pos)

# 각 체스말의 이동 범위 (x,y)
queen_move = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
knight_move = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

# Queen, Knight의 사정거리 안에 있으면 0으로 변환
mark_zero(queen_pos, queen_move)
mark_zero(knight_pos, knight_move)

print(count_element_in_double_list(False, board))
