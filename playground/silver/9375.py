# 패션왕 신해빈

"""
각 종류의 개수 N에서 1개를 뽑는 경우의 수 + 아예 안 뽑는 경우의 수 1

이것을 모든 종류에 대해서 곱한다.

아무것도 안입는 경우는 없으므로 마지막에 1을 빼준다.
"""

import sys
import math
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    dic = defaultdict(int)

    for _ in range(N):
        _, kind = input().strip().split(" ")
        dic[kind] += 1

    res = 1

    for x in dic.values():
        res *= math.comb(x, 1) + 1

    print(res - 1)
