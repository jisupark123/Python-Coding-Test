# 카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

N = int(input())

cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)
cnt = 0

while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    cnt += a + b
    heapq.heappush(cards, a + b)

print(cnt)
