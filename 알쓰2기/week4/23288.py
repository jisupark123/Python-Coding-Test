import sys
from collections import deque


class Dice:
    def __init__(self) -> None:
        self.left = 4
        self.right = 3
        self.front = 2
        self.back = 5
        self.bottom = 6
        self.top = 1
        self.direction = "e"
        self.coordinate = [0, 0]  # y,x

    def get_next_coordinate(self):
        dir_coor = {"e": (0, 1), "w": (0, -1), "n": (-1, 0), "s": (1, 0)}
        return [self.coordinate[i] + dir_coor[self.direction][i] for i in range(2)]

    def roll(self):  # 주사위 굴리기
        self.coordinate = self.get_next_coordinate()
        if self.direction == "e":  # 동
            self.top, self.right, self.bottom, self.left = (
                self.left,
                self.top,
                self.right,
                self.bottom,
            )
        elif self.direction == "w":  # 서
            self.top, self.left, self.bottom, self.right = (
                self.right,
                self.top,
                self.left,
                self.bottom,
            )
        elif self.direction == "s":  # 남
            self.top, self.back, self.bottom, self.front = (
                self.front,
                self.top,
                self.back,
                self.bottom,
            )
        else:  # 북
            self.top, self.front, self.bottom, self.back = (
                self.back,
                self.top,
                self.front,
                self.bottom,
            )

    def rotate_right(self):  # 시계 방향 회전
        if self.direction == "e":
            self.direction = "s"
        elif self.direction == "s":
            self.direction = "w"
        elif self.direction == "w":
            self.direction = "n"
        else:
            self.direction = "e"

    def rotate_left(self):  # 반시계 방향 회전
        if self.direction == "e":
            self.direction = "n"
        elif self.direction == "n":
            self.direction = "w"
        elif self.direction == "w":
            self.direction = "s"
        else:
            self.direction = "e"

    def rotate_opposite(self):  # 반바퀴 회전
        self.rotate_left()
        self.rotate_left()


dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]


def get_score(i, j):
    cnt = 1
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[i][j] = 1
    queue = deque([(i, j)])
    while queue:
        y, x = queue.popleft()
        for a in range(4):
            ny, nx = y + dy[a], x + dx[a]
            if (
                0 <= ny < N
                and 0 <= nx < M
                and board[ny][nx] == board[i][j]
                and visited[ny][nx] == 0
            ):
                cnt += 1
                visited[ny][nx] = 1
                queue.append((ny, nx))

    return cnt


input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dice = Dice()
score = 0
for _ in range(K):
    # 1. 주사위가 이동 방향으로 한 칸 굴러간다. 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.
    ny, nx = dice.get_next_coordinate()
    if not (0 <= ny < N and 0 <= nx < M):
        dice.rotate_opposite()
    dice.roll()

    # 2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
    y, x = dice.coordinate
    score += board[y][x] * get_score(y, x)

    # 3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 이동 방향을 결정한다
    # A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
    # A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
    # A = B인 경우 이동 방향에 변화는 없다.
    A = dice.bottom
    B = board[y][x]
    if A > B:
        dice.rotate_right()
    elif A < B:
        dice.rotate_left()

print(score)
