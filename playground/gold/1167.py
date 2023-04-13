# 트리의 지름

# 아무 노드에서 가장 먼 노드를 찾고 그 노드에서 가장 먼 노드를 찾으면 끝

import sys
from collections import deque

input = sys.stdin.readline

V = int(input())

tree = [[] for _ in range(V + 1)]  # (node,cost)


for _ in range(V):
    lst = map(int, input().strip().split())
    node = next(lst)
    while True:
        n = next(lst)
        if n == -1:
            break
        c = next(lst)
        tree[node].append((n, c))


# def get_max(n):
#     max_node = 0

#     def dfs(prev, curr, total):
#         max_cost = total

#         for node, cost in tree[curr]:
#             if node != prev:
#                 cost = dfs(curr, node, total + cost)
#                 if cost > max_cost:
#                     nonlocal max_node
#                     max_cost = cost
#                     max_node = node

#         return max_cost

#     _max = dfs(-1, n, 0)
#     return (_max, max_node)


def get_max(n):
    max_cost = 0
    max_node = 0
    queue = deque()
    queue.append((n, 0))
    visit = [False for _ in range(V + 1)]
    visit[n] = True
    while queue:
        node, total_cost = queue.popleft()
        if total_cost > max_cost:
            max_cost = total_cost
            max_node = node

        for next_node, next_cost in tree[node]:
            if not visit[next_node]:
                visit[next_node] = True
                queue.append((next_node, total_cost + next_cost))

    return (max_node, max_cost)


node, cost = get_max(1)
print(get_max(node)[1])
