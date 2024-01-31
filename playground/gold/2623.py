# 음악프로그램

"""
모든 정점의 진입 차수를 계산한 배열 생성
진입 차수가 0인 정점들을 큐에 삽입
큐에서 정점을 빼고, 연결된 정점들의 진입 차수 배열을 하나 감소
연결된 정점의 진입 차수 배열이 0이 되었다면, 큐에 해당 정점을 삽입
다시 3으로 돌아가 큐가 빌 때까지 반복
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # graph[n] -> n 다음에 올 가수들
rank = [0] * (N + 1)

for _ in range(M):
    sequence = list(map(int, input().split()))
    for i in range(1, sequence[0]):
        graph[sequence[i]].append(sequence[i + 1])
        rank[sequence[i + 1]] += 1

queue = deque()
ans = []
for i in range(1, N + 1):
    if rank[i] == 0:
        queue.append(i)
        ans.append(i)

while queue:
    x = queue.popleft()
    for nx in graph[x]:
        rank[nx] -= 1
        if rank[nx] == 0:
            queue.append(nx)
            ans.append(nx)

if len(ans) == N:
    print(*ans, sep="\n")
else:
    print(0)

# import sys

# input = sys.stdin.readline

# N, M = map(int, input().split())


# def sorting(start_x, x):
#     for nx in graph[x]:
#         if nx == start_x:  # 루프가 존재하면
#             print(0)
#             exit(0)

#         if not visited[nx]:
#             visited[nx] = 1
#             sorting(start_x, nx)

#     ans.append(x)


# graph = [[] for _ in range(N + 1)]  # graph[n] -> n보다 우선순위가 높은 가수들

# for _ in range(M):
#     sequence = list(map(int, input().split()))
#     for i in range(2, len(sequence)):
#         graph[sequence[i]].append(sequence[i - 1])

# visited = [0] * (N + 1)
# ans = []

# for x in range(1, N + 1):
#     if not visited[x]:
#         visited[x] = 1
#         sorting(x, x)

# for x in ans:
#     print(x)
