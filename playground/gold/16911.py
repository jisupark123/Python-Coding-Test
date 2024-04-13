# 외판원 순회 3

"""
dp + 비트마스킹 사용

|추가된 사항|
- 도시의 정보가 좌표로 주어지기 때문에, 도시간의 거리를 모두 구해놓는다. (인접 행렬 사용)

최소 비용 = f(방문한 도시(N), 현재 방문한 도시(K)) = max of (방문한 도시(N+1), 방문할 곳 K+1) + K->K+1의 비용

방문한 도시들과 현재 방문한 도시가 주어졌을 때, 앞으로 드는 최소 비용을 dp에 저장

2차원 배열로 dp를 만들고, 다음과 같이 설정한다.
행 -> 방문한 도시(비트 마스킹(2진수)을 10진수로 변환한 것), 열 -> 현재 방문한 도시

"""

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())

pos = [list(map(int, input().split())) for _ in range(N)]

# 도시간의 거리
graph = [[0] * N for _ in range(N)]


for i in range(N):
    x, y = pos[i]
    for j in range(N):
        if i != j:
            nx, ny = pos[j]
            graph[i][j] = ((x - nx) ** 2 + (y - ny) ** 2) ** 0.5

dp = [[0] * N for _ in range(2**N)]


def dfs(visited, curr):

    if dp[visited][curr] != 0:
        return dp[visited][curr]

    # 모든 곳에 방문했다면
    if visited == 2**N - 1:

        if graph[curr][start] == 0:  # 출발지로 돌아가는 길이 없다면
            return float("inf")

        return graph[curr][start]

    min_cost = float("inf")
    for x in range(N):

        # 연결되어 있는 노드 & 방문하지 않은 노드
        if graph[curr][x] != 0 and not visited & (1 << (N - x - 1)):
            min_cost = min(
                min_cost,
                dfs(visited | 1 << (N - x - 1), x) + graph[curr][x],
            )

    dp[visited][curr] = min_cost

    return min_cost


start = 0  # 시작은 어디서해도 상관없다
print(dfs(1 << (N - start - 1), start))
