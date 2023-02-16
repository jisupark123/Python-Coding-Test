# 줄 세우기

from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # [인접 노드들]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

res = []


def dfs(i: int):
    visited[i] = True
    if len(graph[i]) == 0:
        return
    for j in graph[i]:
        if not visited[j]:
            dfs(j)
            res.append(j)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        res.append(i)

for num in res[::-1]:
    print(num, end=" ")
# def dfs(lst: list[int]):
#     if len(lst) == 0:
#         return
#     for i in lst:
#         if not visited[i]:
#             visited[i] = True
#             dfs(graph[i])
#             res.append(i)


# for i in range(1, N + 1):
#     if not visited[i]:
#         dfs(graph[i])
#         res.append(i)
