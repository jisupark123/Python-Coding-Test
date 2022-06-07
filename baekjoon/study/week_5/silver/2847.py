# 게임을 만든 동준이

import sys

input = sys.stdin.readline

N = int(input())
scores = [int(input()) for _ in range(N)]

res = 0

for i in range(2, len(scores) + 1):
    if scores[-i] >= scores[-(i - 1)]:
        gap = scores[-i] - scores[-(i - 1)] + 1
        scores[-i] = scores[-i] - gap
        res += gap

print(res)
