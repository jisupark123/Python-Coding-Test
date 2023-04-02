# 그림
import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline


N, M = map(int, input().split())

## 도화지 (이차원 리스트)
picture = [list(map(int, input().split())) for _ in range(N)]

## 방문처리를 위한 리스트
visited = [[False for _ in range(M)] for _ in range(N)]

# 상하좌우 네 방향
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]


# 도화지의 각 지점마다 한번씩 호출
def dfs(cnt, n, m):
    total = 0

    # 방문 처리가 안 된 좌표를 돌면서 1의 합을 저장(total)
    def _dfs(cnt, n, m):
        visited[n][m] = True  # 방문 처리
        nonlocal total
        total += 1
        for d in direction:  # 상하좌우 4방향
            next_n = n + d[0]
            next_m = m + d[1]
            if (
                # 리스트 인덱스 검사
                0 <= next_n < N
                and 0 <= next_m < M
                # 1인지 검사
                and picture[next_n][next_m] == 1
                # 방문하지 않았던 곳인지
                and not visited[next_n][next_m]
            ):
                _dfs(cnt + 1, next_n, next_m)

    _dfs(cnt, n, m)
    return total


res = []
for n in range(N):
    for m in range(M):
        if not visited[n][m] and picture[n][m] == 1:
            res.append(dfs(1, n, m))
if len(res) == 0:
    print(0)
    print(0)
else:
    print(len(res))
    print(max(res))
