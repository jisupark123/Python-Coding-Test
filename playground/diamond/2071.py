# 바둑

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

top_bottom = list(map(int, input().split()))
left_right = list(map(int, input().split()))
left_top_right_bottom = list(map(int, input().split()))
left_bottom_right_top = list(map(int, input().split()))

board = [[0] * len(left_right) for _ in range(len(top_bottom))]
# board = [
#     [0, 0, 0, 1, 0],
#     [0, 1, 1, 0, 1],
#     [0, 1, 0, 0, 1],
#     [0, 0, 1, 1, 1],
#     [0, 0, 0, 0, 1],
# ]


def is_possible_board():
    # top_bottom
    for i in range(N):
        if sum(board[i]) > top_bottom[i]:
            return False

    # left_right
    for i in range(N):
        if sum([board[j][i] for j in range(N)]) > left_right[i]:
            return False

    # left_top_right_bottom
    """
    0 0
    0 1, 1 0
    0 2, 1 1, 2 0
    0 3, 1 2, 2 1, 3 0
    0 4, 1 3, 2 2, 3 1, 4 0
    1 4, 2 3, 3 2, 4 1
    2 4, 3 3, 4 2
    3 4, 4 3
    4 4
    """
    for d in range(N * 2 - 1):
        if (
            sum([board[i][d - i] for i in range(max(0, d - N + 1), min(d, N - 1) + 1)])
            > left_top_right_bottom[d]
        ):
            return False
    """
    4 0
    3 0, 4 1
    2 0, 3 1, 4 2
    1 0, 2 1, 3 2, 4 3
    0 0, 1 1, 2 2, 3 3, 4 4
    0 1, 1 2, 2 3, 3 4
    0 2, 1 3, 2 4
    0 3, 1 4
    0 4
    """

    # left_bottom_right_top
    for d in range(N * 2 - 1):
        if (
            sum(
                board[i][i + d - N + 1]
                for i in range(max(0, N - d - 1), min(N - 1, N * 2 - d - 2) + 1)
            )
            > left_bottom_right_top[d]
        ):
            return False

    return True


# 이중 for문처럼 인덱스 증가
def get_next_idx(i, j):
    if j < N - 1:
        return (i, j + 1)
    if i < N - 1:
        return (i + 1, 0)
    return (-1, -1)


total_stone = sum(top_bottom)  # 총 바둑돌의 개수


stack = [(0, 0)]
i, j = 0, 0

while True:
    i, j = stack[-1]
    if i == -1 and j == -1:
        stack.pop()
        i, j = stack.pop()
        board[i][j] = 0
        ni, nj = get_next_idx(i, j)
        stack.append((ni, nj))
        continue
    # print(stack)
    board[i][j] = 1

    if is_possible_board():  # 유망한지
        if len(stack) == total_stone:  # 바둑판 완성
            break
    else:
        i, j = stack.pop()
        board[i][j] = 0

    stack.append(get_next_idx(i, j))


# 방문 안한 곳의 개수 - 돌의 개수 = 집의 개수 (정답)
not_visited_cnt = N * N
visited = [[0] * N for _ in range(N)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for i in range(N):
    for j in range(N):
        if (
            board[i][j] == 1  # 빈곳인지
            or visited[i][j]  # 이미 검사했는지
            or (i != 0 and i != N - 1 and j != 0 and j != N - 1)  # 1선인지
        ):
            continue

        queue = deque()
        queue.append((i, j))
        visited[i][j] = 1
        not_visited_cnt -= 1
        while queue:
            y, x = queue.popleft()
            for n in range(4):
                ny = y + dy[n]
                nx = x + dx[n]
                if (
                    0 <= ny < N
                    and 0 <= nx < N
                    and board[ny][nx] == 0
                    and not visited[ny][nx]
                ):
                    visited[ny][nx] = 1
                    not_visited_cnt -= 1
                    queue.append((ny, nx))


print(not_visited_cnt - total_stone)
