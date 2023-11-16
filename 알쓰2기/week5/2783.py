# 삼각 김밥

import sys

input = sys.stdin.readline

lst = []

lst.append(list(map(int, input().split())))
for _ in range(int(input())):
    lst.append(list(map(int, input().split())))

print(min(map(lambda x: round(x[0] * (1000 / x[1]), 2), lst)))
