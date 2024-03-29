# # LCA

# """
# A 노드의 조상을 모두 set에 담고
# B 노드의 조상을 탐색하면서 set에 존재하는 순간 출력 후 종료
# """

# import sys


# sys.setrecursionlimit(10**9)

# input = sys.stdin.readline


# def make_tree(parent, child):
#     for x in graph[child]:
#         if x != parent:
#             tree[x] = child
#             make_tree(child, x)


# def dfs1(x):
#     parent = tree[x]
#     if parent != -1:
#         parents_set.add(parent)
#         dfs1(parent)


# def dfs2(x):
#     parent = tree[x]
#     if parent in parents_set:
#         return parent

#     return dfs2(parent)


# N = int(input())

# graph = [[] for _ in range(N + 1)]  # graph[n] -> n과 연결된 노드들
# tree = [-1 for _ in range(N + 1)]  # tree[n] -> n의 부모

# for _ in range(N - 1):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# make_tree(-1, 1)  # tree 만들기

# M = int(input())

# for _ in range(M):

#     a, b = map(int, input().split())

#     parents_set = set()

#     parents_set.add(a)
#     dfs1(a)

#     if b in parents_set:
#         print(b)
#     else:
#         print(dfs2(b))

import sys


sys.setrecursionlimit(10**5)


# 루트노드부터 시작하여 깊이를 구하는 함수
def dfs(now, depth):
    c[now] = True
    d[now] = depth

    for next_ in graph[now]:
        # 깊이를 이미 구한 경우 무시
        if c[next_]:
            continue
        parent[next_] = now
        dfs(next_, depth + 1)


def lca(a, b):
    # 두 노드의 깊이가 다를 경우
    while d[a] != d[b]:
        # 깊이가 큰 노드가 부모 노드로 이동
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 깊이는 같지만 두 노드가 서로 다를 경우
    while a != b:
        # 두 노드를 부모 노드로 이동
        a = parent[a]
        b = parent[b]
    return a


n = int(input())
arr = []
maxN = 0
for _ in range(n - 1):
    x, y = map(int, input().split())
    arr.append([x, y])
    maxN = max(maxN, max([x, y]))

graph = [[] for _ in range(maxN + 1)]
for x, y in arr:
    graph[x].append(y)
    graph[y].append(x)

parent = [0] * (maxN + 1)
d = [0] * (maxN + 1)
c = [0] * (maxN + 1)

dfs(1, 0)  # 루트노드 1 깊이는 0
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))
