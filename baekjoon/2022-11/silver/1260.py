# DFS와 BFS

from collections import deque
from sys import stdin


class Node:
    def __init__(self, key):
        self.key = key  # 인덱스
        self.links: list[int] = []  # 인접 노드들


input = stdin.readline
node_cnt, line_cnt, start_node = map(int, input().split())

graph = [Node(x) for x in range(node_cnt + 1)]  # 그래프 생성

for _ in range(line_cnt):  # 인접 노드 추가
    a, b = map(int, input().split())
    graph[a].links.append(b)
    graph[b].links.append(a)


def dfs():

    visited = [False for _ in range(node_cnt + 1)]  # 방문 처리를 위한 테이블 (노드 개수만큼)
    visited[start_node] = True

    def _dfs(node_idx):
        visited[node_idx] = True  # 방문 처리
        print(node_idx, end=" ")  # 방문 노드 출력
        for i in sorted(graph[node_idx].links):
            if visited[i] == False:
                _dfs(i)

    _dfs(start_node)


def bfs():
    visited = [False for _ in range(node_cnt + 1)]  # 방문 처리를 위한 테이블 (노드 개수만큼)
    visited[start_node] = True
    queue: deque[Node] = deque()
    queue.append(graph[start_node])  # 시작 노드를 먼저 넣어준다.
    while queue:
        node = queue.popleft()
        print(node.key, end=" ")
        for linked_node in sorted(node.links):
            if not visited[graph[linked_node].key]:
                visited[graph[linked_node].key] = True  # 방문 처리
                queue.append(graph[linked_node])  # 인접 노드들을 큐에 추가한다.


dfs()
print()
bfs()
