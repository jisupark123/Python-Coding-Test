import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))


graph = [[int(1e9)] * n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c


for a in range(n):
    for b in range(n):
        for c in range(n):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])


res = 0

for i in range(n):
    item_cnt = 0
    for j in range(n):
        if graph[i][j] <= m:
            item_cnt += items[j]
    res = max(res, item_cnt)

print(res)
