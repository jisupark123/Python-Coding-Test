# 거북이

"""'
가장 왼쪽과 가장 오른쪽의 차이 x 가장 위쪽과 가장 아래쪽의 차이
"""

import sys

input = sys.stdin.readline


class Turtle:
    def __init__(self) -> None:
        self.y = 0
        self.x = 0
        self.d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.di = 0  # 북쪽 (1,0)

    def reset(self):
        self.y = 0
        self.x = 0
        self.di = 0  # 북쪽 (1,0)

    def F(self):
        self.y += self.d[self.di][0]
        self.x += self.d[self.di][1]

    def B(self):
        self.y += -self.d[self.di][0]
        self.x += -self.d[self.di][1]

    def L(self):
        self.di = self.di - 1 if self.di != 0 else 3

    def R(self):
        self.di = self.di + 1 if self.di != 3 else 0


turtle = Turtle()

for _ in range(int(input())):
    turtle.reset()
    min_y, max_y, min_x, max_x = 0, 0, 0, 0
    cmds = input().strip()
    for cmd in cmds:
        if cmd == "F":
            turtle.F()
        elif cmd == "B":
            turtle.B()
        elif cmd == "L":
            turtle.L()
        else:
            turtle.R()
        min_y, max_y, min_x, max_x = (
            min(min_y, turtle.y),
            max(max_y, turtle.y),
            min(min_x, turtle.x),
            max(max_x, turtle.x),
        )
    print((max_y - min_y) * (max_x - min_x))
