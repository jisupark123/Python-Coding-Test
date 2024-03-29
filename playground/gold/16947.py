# 서울 지하철 2호선

"""
1. 순환선에 해당하는 역을 set에 저장한다.
2. 순환선에 해당하지 않는 역마다 bfs로 순환선까지의 최단 거리를 구한다.

순환선 탐지하는 방법
1. 루트 노드를 저장할 roots 배열을 생성
2. 노드를 돌면서 dfs로 루트 노드를 찾는다. 최적화를 위해 같은 root 노드에 연결된 노드들은 한번에 연결한다.
3. 
"""

import sys
from collections import deque

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# """
# 1. 순환선에 해당하는 역을 set에 저장한다.
# 2. 순환선에 해당하지 않는 역마다 bfs로 순환선까지의 최단 거리를 구한다.

# 순환선 탐지하는 방법
# 1. 탐색 순서를 저장할 stack, 탐색 중인 노드를 저장할 visited_set, 순환선에 해당하는 역을 저장할 recurrent_set, 지선에 해당하는 역을 저장할 general_set 생성,
# 2. dfs로 노드 탐색 (visited_set에 없는 노드만 탐색) (순환선은 최소 길이가 3이기 때문에 바로 직전 노드와 다음 노드가 같다면 skip한다.)
# - 탐색하면서 stack과 visited_set에 노드 삽입
# - 탐색하는 노드가 visited_set에 속한다면 탐색 중지, 해당 노드가 나올 때까지 stack의 아이템을 모두 꺼내서 recurrent_set에 넣는다.
# - 가리키는 노드를 하나 탐색했는데 자신이 이미 recurrent_set에 들어갔다면 탐색 중단
# - 탐색하는 노드가 가리키는 모든 노드를 탐색했는데도 recurrent_set에 들어있지 않다면 해당 노드는 general_set에 넣고 stack에서 pop한다.
# """

# import sys
# from collections import deque

# sys.setrecursionlimit(10**8)

# input = sys.stdin.readline


# def dfs(x: int, prev: int):

#     for nx in graph[x]:

#         # 바로 직전 노드는 pass
#         if nx == prev:
#             continue

#         # 이미 방문한 노드라면
#         # 탐색하는 노드가 visited_set에 속한다면 탐색 중지
#         # 해당 노드가 나올 때까지 stack의 아이템을 모두 꺼내서 recurrent_set에 넣는다.
#         if nx in visited:
#             recurrent.add(nx)  # nx는 이 시점에 stack에 없으므로 따로 넣어줌
#             for _ in range(len(stack)):
#                 node = stack.pop()
#                 recurrent.add(node)
#                 if node == nx:
#                     break
#         else:
#             stack.append(nx)
#             visited.add(nx)
#             dfs(nx, x)
#             if x in recurrent:  # 이미 x가 순환선이라고 판별되면 즉시 중단
#                 break

#     if x not in recurrent:
#         general.add(x)
#         stack.pop()
#         visited.discard(x)


# def is_visited(x: int):
#     return x in recurrent or x in general


# N = int(input())

# graph = [[] for _ in range(N + 1)]

# for _ in range(N):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# # 순환선 탐지

# recurrent = set()
# general = set()


# for x in range(1, N + 1):
#     if not is_visited(x):
#         stack = [x]
#         visited = set([x])
#         dfs(x, -1)

# # bfs


# ans = [0] * (N + 1)

# for node in general:
#     queue = deque()
#     queue.append((node, 0))  # node, distance
#     visited = [0] * (N + 1)
#     visited[node] = 1

#     while queue:
#         x, d = queue.popleft()
#         if x in recurrent:
#             ans[node] = d
#             break

#         for nx in graph[x]:
#             if not visited[nx]:
#                 visited[nx] = 1
#                 queue.append((nx, d + 1))

# print(*ans[1:])
