import sys

input = sys.stdin.readline

n = int(input())

graph = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0
        elif graph[i][j] == "Y":
            graph[i][j] = 1
        else:
            graph[i][j] = 1e9


for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


res = []

for i in graph:
    res.append(len(list(filter(lambda x: x != 0 and x <= 2, i))))

print(max(res))
