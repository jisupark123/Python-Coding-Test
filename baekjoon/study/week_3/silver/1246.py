# 온라인 판매

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 달걀 수, 고객 수
P = [int(input()) for _ in range(M)]  # 고객이 제시한 가격

price = 0  # 최소 가격
max_profit = 0  # 최대 수익

for p in sorted(set(P), reverse=True):  # 큰 순서대로 정렬, 중복 값 제거
    profit = (
        len([x for x in P if x >= p]) * p  # 달걀이 고객보다 많으면 달걀수 * 가격
        if N >= len([x for x in P if x >= p])
        else N * p
    )
    if profit >= max_profit:
        price = p
        max_profit = profit


print(price, max_profit)
