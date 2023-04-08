# 트리

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())


# 부모 -> 자식
graph = [[] for _ in range(N)]
parents = list(map(int, input().split()))
root_node = 0
delete_node = int(input())


for i in range(N):
    if parents[i] == -1:
        root_node = i
    else:
        graph[parents[i]].append(i)

if delete_node == root_node:
    print(0)
    exit(0)


# 리프노드 -> 자식이 없거나 delete_node인 경우
res = 0


def dfs(node: int):
    global res
    if len(graph[node]) == 0 or graph[node] == [delete_node]:
        res += 1
        return
    for n in graph[node]:
        if n != delete_node:
            dfs(n)


dfs(root_node)

print(res)
