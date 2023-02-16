# 유기농 배추

T = int(input())


def bfs(i, j, n, m):
    queue: deque[list[int]] = deque()
    queue.append([i, j])
    while len(queue) != 0:
        node = queue.popleft()
        for d in direction:
            if (
                0 <= node[0] + d[0] < n
                and 0 <= node[1] + d[1] < m
                and _map[node[0] + d[0]][node[1] + d[1]] == 1
                and visited[node[0] + d[0]][node[1] + d[1]] == False
            ):
                visited[node[0] + d[0]][node[1] + d[1]] = True
                queue.append([node[0] + d[0], node[1] + d[1]])


from sys import stdin
from collections import deque

input = stdin.readline
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
res = []

for _ in range(T):
    m, n, k = map(int, input().split())
    _map = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    nodes = []
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        nodes.append([y, x])
        _map[y][x] = 1
    for node in nodes:
        if not visited[node[0]][node[1]]:
            bfs(node[0], node[1], n, m)
            cnt += 1
    res.append(cnt)

for i in res:
    print(i)
