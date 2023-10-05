import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split())

# 미로
maze = [input().strip() for _ in range(N)]

# 시작 위치 초기화
start = (0, 0)

for i in range(N):
    for j in range(M):
        if maze[i][j] == "0":
            start = (i, j)
            break

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

queue = deque()

# 시작인덱스y, 시작인덱스x, 열쇠모음, 이동 횟수
queue.append((*start, [0, 0, 0, 0, 0, 0], 0))

# [직전 인덱스y, 직전 인덱스x, 보유한 key(string)]
visited = [[[] for _ in range(M)] for _ in range(N)]


# bfs
while queue:
    # 시작인덱스y, 시작인덱스x, 열쇠모음, 이동 횟수
    y, x, keys, move_cnt = queue.popleft()

    # 출구를 찾을 시 출력 후 프로그램 종료
    if maze[y][x] == "1":
        print(move_cnt)
        exit(0)

    # 4방향
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]

        if (
            # 인덱스 검사
            0 <= ny < N
            and 0 <= nx < M
            # 방문 여부 검사
            and (y, x, keys) not in visited[ny][nx]
            # 벽
            and maze[ny][nx] != "#"
            # key가 필요한지 & 해당 key를 가지고 있는지
            and (
                maze[ny][nx] not in ("A", "B", "C", "D", "E", "F")
                or keys[ord(maze[ny][nx]) - 65] == 1
            )
        ):
            # key 리스트 복사
            copy_keys = keys.copy()

            # key 수집 (아스키코드 활용)
            if maze[ny][nx] in ("a", "b", "c", "d", "e", "f"):
                copy_keys[ord(maze[ny][nx]) - 97] = 1

            # 방문 처리
            visited[ny][nx].append((y, x, copy_keys))

            # queue에 추가
            queue.append((ny, nx, copy_keys, move_cnt + 1))

# 출구 못 찾을 시 -1 출력
print(-1)
