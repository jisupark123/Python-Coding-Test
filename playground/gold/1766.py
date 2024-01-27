# 문제집

"""
1. 우선순위 큐에 root를 모두 넣는다.
2. 가장 작은 수 하나를 뺀다.
3. 2번에 의해 새롭게 root가 되는 수를 모두 넣는다.
4. 2,3 반복
"""

import sys
import heapq

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.parents: set[int] = set()
        self.children: set[int] = set()


N, M = map(int, input().split())

graph = [Node() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].children.add(b)
    graph[b].parents.add(a)

ans = []

# root 노드들로 시작
queue = [x for x in range(1, N + 1) if len(graph[x].parents) == 0]
heapq.heapify(queue)

while len(ans) != N:
    x = heapq.heappop(queue)
    ans.append(x)
    for child in graph[x].children:
        graph[child].parents.discard(x)
        if len(graph[child].parents) == 0:
            heapq.heappush(queue, child)

print(*ans)
