# 친구 네트워크

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    F = int(input())

    def find(v):
        if v != parent[v]:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        p1, p2 = find(v1), find(v2)

        if p1 != p2:
            parent[p2] = p1
            children_cnt[p1] += children_cnt[p2]

        print(children_cnt[p1])

    parent, children_cnt = {}, {}
    for _ in range(F):
        a, b = input().strip().split(" ")

        if a not in parent:
            parent[a] = a
            children_cnt[a] = 1

        if b not in parent:
            parent[b] = b
            children_cnt[b] = 1

        union(a, b)
