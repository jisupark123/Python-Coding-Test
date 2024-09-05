# 그래프의 줄기

import sys

input = sys.stdin.readline

N = int(input())

tree = [set() for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].add(b)
    tree[b].add(a)

edges = [x for x in range(N) if len(tree[x]) == 1]
while len(edges) > 2:
    next_edges = set()
    for edge in edges:
        parent = tree[edge].pop()
        tree[parent].remove(edge)
        next_edges.add(parent)

    edges = [x for x in next_edges if len(tree[x]) == 1]


stems = [x for x in range(N) if len(tree[x]) > 0]

if len(stems):
    print(*stems)
else:
    print(next_edges.pop())
