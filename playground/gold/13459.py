# 구슬 탈출

import sys
from enum import Enum, unique
from copy import deepcopy
from collections import deque

input = sys.stdin.readline


@unique
class Result(Enum):
    SUCCESS = 0
    FAILED = 1
    IN_PROGRESS = 2


@unique
class Direction(Enum):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    TOP = (-1, 0)
    BOTTOM = (1, 0)

    def is_opposite_axis(self, other):
        return (
            self in (Direction.LEFT, Direction.RIGHT)
            and other in (Direction.LEFT, Direction.RIGHT)
        ) or (
            self in (Direction.TOP, Direction.BOTTOM)
            and other in (Direction.TOP, Direction.BOTTOM)
        )


WALL = "#"
BLANK = "."
RED = "R"
BLUE = "B"
HOLE = "O"


class Board:
    def __init__(self, board):
        self.board = board
        self.red_pos = None
        self.blue_pos = None
        self.hole_pos = None
        self.init()

    def init(self):
        for i in range(N):
            for j in range(M):
                if self.board[i][j] == HOLE:
                    self.hole_pos = (i, j)
                elif self.board[i][j] == RED:
                    self.red_pos = (i, j)
                elif self.board[i][j] == BLUE:
                    self.blue_pos = (i, j)

    def tilt(self, direction):
        direction_vector = direction.value
        if direction == Direction.LEFT:
            first_ball = RED if self.red_pos[1] < self.blue_pos[1] else BLUE
        elif direction == Direction.RIGHT:
            first_ball = RED if self.red_pos[1] > self.blue_pos[1] else BLUE
        elif direction == Direction.TOP:
            first_ball = RED if self.red_pos[0] < self.blue_pos[0] else BLUE
        else:  # Bottom
            first_ball = RED if self.red_pos[0] > self.blue_pos[0] else BLUE

        new_board = deepcopy(self.board)
        red_result = Result.IN_PROGRESS
        blue_result = Result.IN_PROGRESS

        if first_ball == RED:
            new_board, red_result = self._move_ball(
                new_board, RED, self.red_pos, direction_vector
            )
            new_board, blue_result = self._move_ball(
                new_board, BLUE, self.blue_pos, direction_vector
            )

        else:
            new_board, blue_result = self._move_ball(
                new_board, BLUE, self.blue_pos, direction_vector
            )
            new_board, red_result = self._move_ball(
                new_board, RED, self.red_pos, direction_vector
            )

        if blue_result == Result.SUCCESS:
            return None, Result.FAILED
        if red_result == Result.SUCCESS:
            return None, Result.SUCCESS
        return Board(new_board), Result.IN_PROGRESS

    def _move_ball(self, board, ball_color, curr_pos, direction_vector):
        board[curr_pos[0]][curr_pos[1]] = BLANK
        next_pos = (
            curr_pos[0] + direction_vector[0],
            curr_pos[1] + direction_vector[1],
        )
        while board[next_pos[0]][next_pos[1]] == BLANK:
            curr_pos = next_pos
            next_pos = (
                curr_pos[0] + direction_vector[0],
                curr_pos[1] + direction_vector[1],
            )

        if next_pos == self.hole_pos:
            return board, Result.SUCCESS

        board[curr_pos[0]][curr_pos[1]] = ball_color
        return board, Result.IN_PROGRESS

    def __hash__(self):
        return hash((self.red_pos, self.blue_pos))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def display(self):
        print()
        for line in self.board:
            print("".join(line))


N, M = map(int, input().split())


def sol():
    init_state = Board([list(input().strip()) for _ in range(N)])
    visited = set()
    queue = deque([(init_state, 0)])  # (board, moves)

    while queue:
        current_board, moves = queue.popleft()

        if moves < 10:
            for direction in Direction:
                next_board, result = current_board.tilt(direction)
                board_hash = hash(next_board)
                if board_hash not in visited:
                    if result == Result.SUCCESS:
                        return 1

                    if result == Result.IN_PROGRESS:
                        visited.add(board_hash)
                        queue.append((next_board, moves + 1))
    return 0


print(sol())
