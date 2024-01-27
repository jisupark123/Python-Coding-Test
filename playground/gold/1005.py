# ACM Craft

"""
방법 1 
- 우선 순위의 건물을 모두 짓지 않으면 다음 건물로 넘어가지 않도록 구현 
- 진입 차수 활용

방법 2
- 먼저 위상 정렬을 해놓고 다이나믹 프로그래밍 기법을 활용
- 채점 95%에서 에러나는데 이유를 모르겠음
"""
import sys
from collections import deque

input = sys.stdin.readline


def ACM_Craft():
    N, K = map(int, input().split())

    graph = [[] for _ in range(N + 1)]  # graph[n] -> n 다음에 지어야 하는 건물들
    indegree = [0] * (N + 1)  # 진입 차수 (해당 건물보다 먼저 지어야 하는 건물의 개수)

    time = [0] + list(map(int, input().split()))
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    ans = [0] * (N + 1)
    dq = deque()

    # 진입차수가 0인것부터 시작
    for i in range(1, N + 1):
        if indegree[i] == 0:
            dq.append(i)
            ans[i] = time[i]

    while dq:
        x = dq.popleft()

        for nx in graph[x]:
            ans[nx] = max(time[nx] + ans[x], ans[nx])
            indegree[nx] -= 1
            if indegree[nx] == 0:
                dq.append(nx)

    print(ans[w])


for _ in range(int(input())):
    ACM_Craft()


# import sys

# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline


# def ACM_Craft():
#     class Node:
#         def __init__(self):
#             self.parents = []
#             self.children = []

#     # 위상 정렬
#     def sorting(x):
#         for parent in graph[x].parents:
#             if not visited[parent]:
#                 visited[parent] = 1
#                 sorting(parent)
#         sorted_node.append(x)

#     N, K = map(int, input().split())

#     times = [0] + list(map(int, input().split()))
#     graph = [Node() for _ in range(N + 1)]  # graph[n] -> n보다 먼저 지어야하는 건물들

#     for _ in range(K):
#         a, b = map(int, input().split())
#         graph[a].children.append(b)
#         graph[b].parents.append(a)

#     W = int(input())

#     visited = [0] * (N + 1)
#     sorted_node = []

#     sorting(W)
#     root = sorted_node[0]

#     res = [0] * (N + 1)
#     res[root] = times[root]
#     set_sorted_node = set(sorted_node)

#     for x in sorted_node[1:]:
#         max_parent = max([res[a] for a in graph[x].parents if a in set_sorted_node])
#         res[x] = max_parent + times[x]

#     print(res[W])


# for _ in range(int(input())):
#     ACM_Craft()
