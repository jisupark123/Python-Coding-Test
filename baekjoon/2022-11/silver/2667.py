# 단지번호붙이기

from sys import stdin

input = stdin.readline

# map의 인접한 노드를 순회하면서 방문한 곳은 visited에 저장하고 개수를 반환함
# visited에 기록된 노드는 return
def dfs(x, y):
    def _dfs(x, y):
        nonlocal cnt
        if visited[x][y]:
            return
        cnt += 1
        visited[x][y] = True
        for d in direction:
            if (
                0 <= x + d[0] < N
                and 0 <= y + d[1] < N
                and _map[x + d[0]][y + d[1]] == "1"
                and visited[x + d[0]][y + d[1]] == False
            ):
                _dfs(x + d[0], y + d[1])

    cnt = 0
    _dfs(x, y)
    return cnt


N = int(input())
_map = [input().strip() for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
res = []
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for i in range(N):
    for j in range(N):
        if _map[i][j] == "1" and visited[i][j] == False:
            res.append(dfs(i, j))

res.sort()
print(len(res))
for i in res:
    print(i)
