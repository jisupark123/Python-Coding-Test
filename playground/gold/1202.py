# 보석 도둑

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: (x[1], x[0]), reverse=True)
bags.sort(reverse=True)

print(jewels)
print(bags)
