# BFS 스페셜 저지

"""
- 고려해야 할 것
-> 부모가 큐에 들어간 순서대로 자식이 나와야 한다.
-> 단순히 차수만 따지면 안된다.
-> 자식 노드의 인덱스를 계산해서 정답 여부를 판별
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

user_ans = list(map(int, input().split()))

visited = [0] * (N + 1)
visited[1] = 1

children = [set() for _ in range(N + 1)]

queue = deque()
queue.append(1)  # 정점

while queue:
    node = queue.popleft()

    for child in graph[node]:
        if not visited[child]:
            visited[child] = 1
            children[node].add(child)
            queue.append(child)


ans = 1
next_idx = 1  # 자식 노드의 시작 인덱스

for x in user_ans:
    if next_idx == N:
        break
    child_len = len(children[x])
    a = set(user_ans[next_idx : next_idx + child_len])
    b = children[x]

    # 입력으로 주어진 자식의 인덱스와 bfs로 계산한 자식의 인덱스가 다르면 틀린 답
    if a != b:
        ans = 0
        break
    next_idx += child_len

print(ans)
