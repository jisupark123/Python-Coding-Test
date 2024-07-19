# 아이들과 선물 상자

import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

c = list(map(lambda x: -int(x), input().split()))
w = list(map(int, input().split()))

heapq.heapify(c)


for i in range(M):
    if not c:
        print(0)
        exit(0)

    item = -heapq.heappop(c)
    if w[i] > item:
        print(0)
        exit(0)

    if w[i] < item:
        heapq.heappush(c, -(item - w[i]))

print(1)
