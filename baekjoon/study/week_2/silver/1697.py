# 숨바꼭질

from collections import deque


def bfs(MAX, start, target):
    dist = [0] * (MAX + 1)
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == target:
            return dist[x]

        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)


MAX = 100000
N, K = map(int, input().split())
print(bfs(MAX, N, K))
