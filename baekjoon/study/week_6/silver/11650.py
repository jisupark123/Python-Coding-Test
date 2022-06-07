# 좌표 정렬하기

import sys

input = sys.stdin.readline

N = int(input())
coordinates = [tuple(map(int, input().split())) for _ in range(N)]

for x in sorted(coordinates, key=lambda x: (x[0], x[1])):
    print(x[0], x[1])
