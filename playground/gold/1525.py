# 퍼즐

"""
퍼즐의 상태를 hash로 변경해야 함 -> 2차원 tuple 사용

hash로 변환된 퍼즐의 상태를 set에 저장하고 방문하지 않은 곳만 bfs로 탐색
"""

import sys
from collections import deque

input = sys.stdin.readline

puzzle = tuple([tuple(map(int, input().split())) for _ in range(3)])

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

in_range = lambda y, x: 0 <= y < 3 and 0 <= x < 3


def is_completed(puzzle):
    return puzzle == ((1, 2, 3), (4, 5, 6), (7, 8, 0))


def move(puzzle):
    zero_pos = ()
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == 0:
                zero_pos = (i, j)
                break

    for a in range(4):
        ny, nx = zero_pos[0] + dy[a], zero_pos[1] + dx[a]
        if in_range(ny, nx):
            new_puzzle = []
            for y in range(3):
                tmp = []
                for x in range(3):
                    if (y, x) == zero_pos:
                        tmp.append(puzzle[ny][nx])
                    elif (y, x) == (ny, nx):
                        tmp.append(0)
                    else:
                        tmp.append(puzzle[y][x])

                new_puzzle.append(tuple(tmp))

            yield tuple(new_puzzle)


visit = set()
visit.add(puzzle)

q = deque()
q.append((puzzle, 0))  # puzzle, time

while q:
    puz, time = q.popleft()
    if is_completed(puz):
        print(time)
        exit(0)

    for npuz in move(puz):
        if not npuz in visit:
            visit.add(npuz)
            q.append((npuz, time + 1))

print(-1)
