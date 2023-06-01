# 트리의 지름

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

root = 1


def get_max_length(start_node):
    max_node = 0
    max_weight = 0
    visited = [False] * (N + 1)
    visited[start_node] = True
    queue = deque()
    queue.append((start_node, 0))  # node,weight

    while queue:
        node, weight = queue.popleft()
        if weight > max_weight:
            max_weight = weight
            max_node = node
        for next_node, next_weight in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, weight + next_weight))

    return (max_node, max_weight)


node1, _ = get_max_length(root)
node2, weight = get_max_length(node1)
print(weight)
