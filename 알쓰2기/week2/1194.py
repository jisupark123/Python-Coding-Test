import sys
from collections import deque


def keys_to_num(keys: list[int]):
    num = 0
    for i in range(len(keys)):
        num += 0 if keys[i] == 0 else (keys[i] + 1) ** i
    return num


input = sys.stdin.readline

N, M = map(int, input().split())

maze = [input().strip() for _ in range(N)]

start = (0, 0)

for i in range(N):
    for j in range(M):
        if maze[i][j] == "0":
            start = (i, j)
            break

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

queue = deque()
queue.append((*start, [0, 0, 0, 0, 0, 0], 0))  # 시작인덱스y, 시작인덱스x, 열쇠모음, 이동 횟수
visited = [[[] for _ in range(M)] for _ in range(N)]  # 어디서 왔는지 (y,x)


while queue:
    y, x, keys, cnt = queue.popleft()

    key_num = keys_to_num(keys)
    if maze[y][x] == "1":
        print(cnt)
        exit(0)
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]

        # if 0 <= ny < N and 0 <= nx < M:
        #     print(y, x, keys, cnt, key_num)
        if (
            0 <= ny < N
            and 0 <= nx < M
            and (y, x, key_num) not in visited[ny][nx]
            and maze[ny][nx] != "#"
            and (
                maze[ny][nx] not in ("A", "B", "C", "D", "E", "F")
                or keys[ord(maze[ny][nx]) - 65] == 1
            )
        ):
            copy_keys = keys.copy()
            if maze[ny][nx] in ("a", "b", "c", "d", "e", "f"):
                copy_keys[ord(maze[ny][nx]) - 97] = 1
            visited[ny][nx].append((y, x, key_num))
            queue.append((ny, nx, copy_keys, cnt + 1))

print(-1)
