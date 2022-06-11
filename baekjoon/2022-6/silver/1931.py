# 회의실 배정

import sys

input = sys.stdin.readline

N = int(input())

times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))

res = 1
curr = times[0]

for i in range(1, len(times)):
    if times[i][0] >= curr[1]:
        curr = times[i]
        res += 1

print(res)
