# 바이러스

from sys import stdin
from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.links = []


input = stdin.readline

node_cnt = int(input())
line_cnt = int(input())

lines = [list(map(int, input().split())) for _ in range(line_cnt)]
graph = [Node(x) for x in range(node_cnt + 1)]

for line in lines:
    graph[line[0]].links.append(line[1])
    graph[line[1]].links.append(line[0])

visited = [False for _ in range(node_cnt + 1)]
visited[1] = True
queue: deque[Node] = deque()
queue.append(graph[1])

res = 0

while len(queue) != 0:
    node = queue.popleft()
    res += 1
    for linked_node in sorted(node.links):
        if visited[graph[linked_node].key] == False:
            queue.append(graph[linked_node])
            visited[graph[linked_node].key] = True

print(0 if res == 0 else res - 1)
