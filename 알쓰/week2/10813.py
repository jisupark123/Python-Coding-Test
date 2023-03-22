# 공 바꾸기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

balls = list(range(1, N + 1))
change = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

for c in change:
    balls[c[0]], balls[c[1]] = balls[c[1]], balls[c[0]]

for ball in balls:
    print(ball, end=" ")
