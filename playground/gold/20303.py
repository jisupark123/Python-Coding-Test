# 할로윈의 양아치

"""
아이들을 그룹으로 묶어서 배낭문제로 변환해야 함

k - 그룹에 속한 아이의 수 (사탕을 뺏었을 때 우는 아이의 수)
v - 그룹이 보유한 사탕 수

f(i, j) 
-> i번째 그룹부터 고려하고 j명이 우는 것까지 혀용될 때, 얻을 수 있는 최대 사탕의 수
-> max(f(i+1, j), f(i+1, j-k[i]) + v[i])
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline
from collections import defaultdict


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        a, b = b, a
    parent[a] = b


N, M, K = map(int, input().split())

c = list(map(int, input().split()))

parent = [x for x in range(N)]


for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    union(a, b)


k = defaultdict(int)  # 그룹에 속한 아이의 수 (사탕을 뺏었을 때 우는 아이의 수)
v = defaultdict(int)  # 그룹이 보유한 사탕 수

for i in range(N):
    k[find(parent[i])] += 1
    v[find(parent[i])] += c[i]

k = [k[key] for key in sorted(k.keys())]
v = [v[key] for key in sorted(v.keys())]


# f(i, j)
# -> i번째 그룹까지 고려하고 j명이 우는 것까지 혀용될 때, 얻을 수 있는 최대 사탕의 수
# -> max(f(i-1, j), f(i-1, j-k[i]) + v[i])


dp = [[0] * (K + 1) for _ in range(len(k))]
for i in range(K + 1):
    dp[0][i] = v[0] if k[0] < i else 0


for i in range(1, len(k)):
    for j in range(K + 1):
        dp[i][j] = dp[i - 1][j]
        if j - k[i] > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - k[i]] + v[i])

print(dp[len(k) - 1][K])
