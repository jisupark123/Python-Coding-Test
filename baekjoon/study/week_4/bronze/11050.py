# 이항계수

# nCk 조합 구하기

from itertools import combinations


N, K = map(int, input().split())
N = list(range(1, N + 1))

print(len(list(combinations(N, K))))
