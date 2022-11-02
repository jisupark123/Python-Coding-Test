# 배열 돌리기 1

# 1. 돌릴 수 있는지 확인
# 2. 돌린다 (돌리는 깊이 -> min(N,M) // 2)
# 3. 안쪽 돌릴 수 있는지 확인
# 4. 돌린다
#
#
#

from sys import stdin


input = stdin.readline

N, M, R = map(int, input().split())


array = [list(map(int, input().split())) for _ in range(N)]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 시계 방향 회전


def rotate_list(start, height, width):
    temp = array[start][start]
    i, j = start, start
    for direction in directions:
        while True:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if not (start <= new_i <= start + height - 1) or not (
                start <= new_j <= start + width - 1
            ):
                break
            array[i][j] = array[new_i][new_j]
            i = new_i
            j = new_j

            if i == start and j == start:  # 처음으로 돌아오면 break
                break

    array[start + 1][start] = temp
    return


for _ in range(R):
    h, w = N, M
    for d in range(min(N, M) // 2):  # 돌리는 깊이
        rotate_list(d, h, w)
        h -= 2
        w -= 2


for row in array:
    print(" ".join(map(str, row)))
