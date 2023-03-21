# 연결 요소의 개수
# 각 정점을 하나씩 순회하면서 dfs를 돌린다.
# dfs를 돌리면서 들린 노드는 방문 처리를 해주고 이미 방문한 노드는 pass 한다.
# 방문 처리가 안된 노드를 순회한 개수가 정답

import sys

sys.setrecursionlimit(100000000)


def dfs(i):
    if visited[i]:
        return
    visited[i] = True
    for j in graph[i]:
        dfs(j)


input = sys.stdin.readline
node_cnt, edge_cnt = map(int, input().split())

graph = [[] for _ in range(node_cnt)]
visited = [False for _ in range(node_cnt)]
res = 0

for _ in range(edge_cnt):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)  # 양방향 연결 리스트이므로 양쪽에서 연결해야 한다.

for i in range(node_cnt):
    if not visited[i]:
        res += 1
        dfs(i)
print(res)
