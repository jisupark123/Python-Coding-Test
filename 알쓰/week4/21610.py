# 마법사 상어와 비바라기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(M)]
clouds = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
cloud_memo = [[0 for _ in range(N)] for _ in range(N)]

# ← ↖ ↑ ↗ → ↘ ↓ ↙
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


# cloud -> (row,col)
# move -> (방향,스칼라) -> 어느 방향으로 얼만큼 이동할건지
def move_cloud(cloud, move):
    y = (cloud[0] + (direction[move[0] - 1][0] * move[1])) % N
    x = (cloud[1] + (direction[move[0] - 1][1] * move[1])) % N
    cloud_memo[y][x] = 1  # 구름 표시
    return (y, x)


# 물복사버그 마법
# 대각선 4곳 중에 물이 0이상 있는 곳이 몇개인지
def water_copy_bug(r, c):
    cnt = 0
    # ↖ ↗ ↘ ↙
    for d in direction[1::2]:
        if 0 <= r + d[0] < N and 0 <= c + d[1] < N and grid[r + d[0]][c + d[1]] > 0:
            cnt += 1
    return cnt


for move in moves:
    # 1. 모든 구름이 move[0] 방향으로 move[1]칸 이동한다.
    clouds = list(map(lambda x: move_cloud(x, move), clouds))

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    for cloud in clouds:
        grid[cloud[0]][cloud[1]] += 1

    # 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다.
    for cloud in clouds:
        grid[cloud[0]][cloud[1]] += water_copy_bug(cloud[0], cloud[1])

    # 구름이 있었던 칸을 제외한 나머지 칸 중에서 물의 양이 2 이상인 칸에 구름이 생긴다.
    # 구름이 생기면 물의 양이 2만큼 줄어든다.
    new_clouds = []
    for r in range(N):
        for c in range(N):
            # if grid[r][c] >= 2 and (r, c) not in clouds:
            if grid[r][c] >= 2 and cloud_memo[r][c] == 0:
                grid[r][c] -= 2
                new_clouds.append((r, c))

    for c in clouds:
        cloud_memo[c[0]][c[1]] = 0  # 구름 제거
    clouds = new_clouds


res = 0
for g in grid:
    res += sum(g)

print(res)
