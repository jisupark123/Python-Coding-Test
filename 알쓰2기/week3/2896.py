# 무알콜 칵테일

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

i, j, k = map(int, input().split())

cocktail_cnt = min(map(lambda x: x[0] / x[1], zip([a, b, c], [i, j, k])))
for num in map(lambda x: x[0] - (x[1] * cocktail_cnt), zip([a, b, c], [i, j, k])):
    print(num, end=" ")
