# 등수 매기기

"""
1. 예상 등수를 정렬한다.
2 for문을 돌면서 정렬된 등수와 예상 등수의 차이를 결과값에 더한다.
"""

import sys

input = sys.stdin.readline

N = int(input())

rank = [int(input()) for _ in range(N)]
rank.sort()

res = 0
for i, rank in enumerate(rank):
    res += abs((i + 1) - rank)
print(res)
