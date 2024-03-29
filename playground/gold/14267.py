# 회사 문화 1

"""
루트부터 dfs로 내려오면서 가중치를 전달한다.
만약 내려온 가중치 외에 input으로 들어온 가중치가 있다면 2개의 가중치를 더해서 전파한다.
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, m = map(int, input().split())

tree = [[] for _ in range(n + 1)]  # tree[n] -> n의 부하들

compliments = [0] * (n + 1)

for i, node in enumerate(map(int, input().split()), 1):
    if node != -1:
        tree[node].append(i)

for _ in range(m):
    i, w = map(int, input().split())
    compliments[i] += w

ans = [0] * (n + 1)


def propagation(x, weight):
    cw = weight + compliments[x]
    ans[x] = cw
    for child in tree[x]:
        propagation(child, cw)


propagation(1, 0)

print(*ans[1:])
