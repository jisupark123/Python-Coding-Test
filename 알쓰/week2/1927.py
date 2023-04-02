# 최소 힙

import sys
import heapq

input = sys.stdin.readline

N = int(input())

queue = []

for _ in range(N):
    n = int(input())
    if n == 0:
        if len(queue):
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, n)
