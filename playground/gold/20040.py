# 사이클 게임

"""
union-find

A,B를 이을 때 이미 같은 집합에 속해 있다면 사이클 발생
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    parents[find(a)] = find(b)


n, m = map(int, input().split())

lines = [list(map(int, input().split())) for _ in range(m)]

parents = [x for x in range(n)]

for i, (a, b) in enumerate(lines, 1):
    if find(a) == find(b):
        print(i)
        exit(0)
    union(a, b)

print(0)
