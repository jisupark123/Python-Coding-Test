# 문제집

"""
1. 우선순위 큐에 각 집합의 대표를 모두 넣는다.
2. 가장 작은 수 하나를 뺀다.
3. 2번에 의해 새롭게 대표가 되는 문제를 모두 우선순위 큐에 넣는다.
4. 2,3 반복
"""

import sys
import heapq

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.parents: set[int] = set()  # 해당 문제보다 먼저 풀어야 하는 문제들
        self.children: set[int] = set()  # 해당 문제보다 나중에 풀어야 하는 문제들


N, M = map(int, input().split())

graph = [Node() for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].children.add(b)
    graph[b].parents.add(a)

ans = []  # 결과 리스트

# 대표 문제들로 시작
# 대표 문제 -> 먼저 풀어야 하는 문제가 없는 문제
queue = [x for x in range(1, N + 1) if len(graph[x].parents) == 0]
heapq.heapify(queue)

while len(ans) != N:
    x = heapq.heappop(queue)  # 가장 작은 수 하나를 뺀다.
    ans.append(x)  # 결과 리스트에 추가

    # x를 parents로 가지고 있는 노드에서 x를 제거한다.
    for child in graph[x].children:
        graph[child].parents.discard(x)  # set에서 원소를 제거하는 시간 복잡도 O(1)

        if len(graph[child].parents) == 0:  # 새롭게 대표가 되는 문제를 모두 우선순위 큐에 넣는다.
            heapq.heappush(queue, child)

print(*ans)
