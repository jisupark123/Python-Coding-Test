# 최종 순위

"""
1. 각 팀의 관계를 담은 그래프를 인접 행렬로 생성 (N이 최대 500)
2. 바뀐 등수를 그래프에 반영
3. 위상정렬 수행
-> 사이클 발생 시 'IMPOSSIBLE' 출력
-> 중간에 indegree가 0인 정점이 여러개 있다면'?' 출력
"""

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    rank = list(map(int, input().split()))

    graph = [
        [0] * (N + 1) for _ in range(N + 1)
    ]  # graph[i][j]가 1이면 i가 j보다 높은 등수
    for i in range(N - 1):
        for j in range(i + 1, N):
            graph[rank[i]][rank[j]] = 1

    M = int(input())

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b], graph[b][a] = graph[b][a], graph[a][b]

    indegree = [0] * (N + 1)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if graph[i][j] == 1 and i != j:
                indegree[j] += 1

    q = deque([x for x in range(1, N + 1) if indegree[x] == 0])

    cycle = False

    if len(q) == 0:
        cycle = True

    ans = []
    many_ans = False
    while q and not cycle:

        if len(q) > 1:
            many_ans = True

        x = q.popleft()
        ans.append(x)

        for nx in range(1, N + 1):
            if graph[x][nx] == 1 and x != nx:
                indegree[nx] -= 1
                if indegree[nx] == 0:
                    q.append(nx)

                elif indegree[nx] < 0:  # cycle
                    cycle = True
                    break

    # 독립된 노드가 존재하는 경우 최초 큐에서 사이클을 잡아내지 못함
    # 따라서 len(ans)를 한번 더 확인
    if cycle or len(ans) < N:
        print("IMPOSSIBLE")
    elif many_ans:
        print("?")
    else:
        print(*ans)
