# 웜홀

import sys

input = sys.stdin.readline


def bf(start):
    dist[start] = 0
    for i in range(1, n + 1):
        for s in range(1, n + 1):
            for next, time in graph[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    if i == n:  # n번 이후에도 값이 갱신되면 음수 사이클 존재.
                        return True
    return False


TC = int(input())
for i in range(TC):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [10001 for _ in range(n + 1)]
    for j in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for k in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    negative_cycle = bf(1)
    if not negative_cycle:
        print("NO")
    else:
        print("YES")
