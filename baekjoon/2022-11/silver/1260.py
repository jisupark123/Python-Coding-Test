# DFS와 BFS

from collections import deque
from sys import stdin


class Node:
    def __init__(self, key):
        self.key = key
        self.links = []


def dfs(graph: list[Node]):
    def _dfs(node_idx):
        visited[node_idx] = True
        print(node_idx, end=" ")
        for i in sorted(graph[node_idx].links):
            if visited[i] == False:
                _dfs(i)

    visited = [False for _ in range(node_cnt + 1)]
    visited[start_node] = True
    _dfs(start_node)


def bfs(graph: list[Node]):
    visited = [False for _ in range(node_cnt + 1)]
    visited[start_node] = True
    queue: deque[Node] = deque()
    queue.append(graph[start_node])
    while len(queue) != 0:
        node = queue.popleft()
        print(node.key, end=" ")
        for linked_node in sorted(node.links):
            if visited[graph[linked_node].key] == False:
                queue.append(graph[linked_node])
                visited[graph[linked_node].key] = True

    visited = [False for _ in range(node_cnt + 1)]
    visited[start_node] = True
    bfs(start_node)


input = stdin.readline
node_cnt, line_cnt, start_node = map(int, input().split())

lines = [list(map(int, input().split())) for _ in range(line_cnt)]


graph = [Node(x) for x in range(node_cnt + 1)]

for line in lines:
    graph[line[0]].links.append(line[1])
    graph[line[1]].links.append(line[0])


dfs(graph)
print()
bfs(graph)
