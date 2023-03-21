# 안전 영역

import sys

input = sys.stdin.readline

N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

for i in info:
    print(i)
