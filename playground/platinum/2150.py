# Strongly Connected Component

"""
코사라주 알고리즘

1. 역방향 그래프를 생성
2. dfs 탐색 순서대로 모든 정점을 stack에 push
3. stack에서 pop되는 순서대로 역방향 그래프에서 dfs 수행
-> 정점으로부터 탐색되는 정점을 scc로 묶음

"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
reversed_graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    reversed_graph[b].append(a)


def dfs(x):
    visited[x] = 1
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx)
    stack.append(x)


stack = []
visited = [0] * (V + 1)

for x in range(1, V + 1):
    if not visited[x]:
        dfs(x)


def reversed_dfs(x):
    visited[x] = 1
    for nx in reversed_graph[x]:
        if not visited[nx]:
            reversed_dfs(nx)
    scc.append(x)


visited = [0] * (V + 1)
ans = []

for x in stack[::-1]:
    scc = []
    if not visited[x]:
        reversed_dfs(x)
        ans.append(sorted(scc))

ans.sort(key=lambda x: min(x))
print(len(ans))
for a in ans:
    print(*a, -1)


"""
타잔 알고리즘

1. 역방향 그래프를 생성
2. 모든 원소들에 대해 다음을 수행

ans -> scc 개수

scc의 발견 조건 -> 정점이 해당 정점의 부모 정점으로 갈 수 있는지

1) 연결된 원소를 stack에 push (stack이 비어있다면 처음 원소를 push)
2) 이전 원소 외에 연결된 원소가 존재한다면 -> 1번으로
3) 연결된 원소가 이전 원소가 유일하다면
3) (존재하지 않는다면) stack
"""


# import sys

# input = sys.stdin.readline

# V, E = map(int, input().split())

# graph = [[] for _ in range(V + 1)]

# for _ in range(E):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# visited = [0] * (V + 1)


# def dfs(x):
#     stack.append(x)
#     scc = True

#     for nx in graph[x]:
#         if visited[nx] == 0:
#             visited[nx] = True
#             dfs(x, nx)
#         else:
#             scc = False

#     return scc


# stack = []
# ans = 0
