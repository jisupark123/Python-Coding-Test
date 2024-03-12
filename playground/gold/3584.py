# 가장 가까운 공통 조상

"""
A 노드의 조상을 모두 set에 담고
B 노드의 조상을 탐색하면서 set에 존재하는 순간 출력 후 종료
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    tree = [-1 for _ in range(N + 1)]  # tree[n] -> n의 부모

    for _ in range(N - 1):
        parent, child = map(int, input().split())
        tree[child] = parent

    a, b = map(int, input().split())

    parents_set = set()

    def dfs1(x):
        parent = tree[x]
        if parent != -1:
            parents_set.add(parent)
            dfs1(parent)

    def dfs2(x):
        parent = tree[x]
        if parent in parents_set:
            return parent

        return dfs2(parent)

    parents_set.add(a)
    dfs1(a)

    if b in parents_set:
        print(b)
    else:
        print(dfs2(b))
