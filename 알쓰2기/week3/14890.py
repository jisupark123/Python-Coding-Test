# 경사로

"""
경사로는 낮은 칸과 높은 칸을 연결하며, 아래와 같은 조건을 만족해야한다.

1. 경사로는 낮은 칸에 놓으며, L개의 연속된 칸에 경사로의 바닥이 모두 접해야 한다.
2. 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
3. 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, L개의 칸이 연속되어 있어야 한다.


아래와 같은 경우에는 경사로를 놓을 수 없다.

1. 경사로를 놓은 곳에 또 경사로를 놓는 경우
2. 낮은 칸과 높은 칸의 높이 차이가 1이 아닌 경우
3. 낮은 지점의 칸의 높이가 모두 같지 않거나, L개가 연속되지 않은 경우
4. 경사로를 놓다가 범위를 벗어나는 경우


"""
import sys

input = sys.stdin.readline
N, L = map(int, input().split())

# 입력받은 2차원 리스트
_map = [list(map(int, input().split())) for _ in range(N)]

res = 0  # 결과값

"""
j+1이 j랑 같다면 j+=1
j+1이 j랑 절댓값이 2이상 차이난다면 길이 없는 것

j+1이 j보다 1 낮다면
1. j+L이 N보다 크다면 길이 없는 것(경사로가 삐져나감)
2. j+1,...,j+L이 모두 j-1이라면 모두 -1로 바꾸고(경사로 놓기) j+=L+1
3. 2번에 해당하지 않다면 길이 없는 것 (경사로를 놓을 수 없음)

j + 1이 j보다 1 크다면
1. j+1-L이 0보다 작다면 길이 없는 것(경사로가 삐져나감)
2. j,...,j-L+1이 모두 j라면 모두 -1로 바꾸고(경사로 놓기) j+=L+1
3. 2번에 해당하지 않다면 길이 없는 것 (경사로를 놓을 수 없음)
"""


# 모든 행을 for loop으로 돌면서 지나갈 수 있는 길의 개수를 구한다.
def road_cnt():
    cnt = 0  # 지나갈 수 있는 길의 개수

    for i in range(N):  # 행 검사
        row = _map[i]  # 원본 row
        copy_row = row.copy()  # 복사본 row (경사로를 놓은 칸을 저장)
        j = 0
        is_road = True  # 길이 있는지 없는지

        # j가 끝까지(N-1) 가면 길이 있다고 판정
        while j < N - 1:
            # 현재 칸과 다음 칸이 평행하다면 통과
            if row[j] == row[j + 1]:
                j += 1

            # 현재 칸과 다음 칸의 높이 차가 2이상이면 길이 없음
            elif abs(row[j] - row[j + 1]) > 1:
                is_road = False
                break

            # 다음 칸이 더 낮을 때
            elif row[j] > row[j + 1]:
                # 경사로를 놓아도 범위를 벗어나는 경우 - 길이 없음
                if j + L >= N:
                    is_road = False
                    break

                # 경사로를 놓을 칸들의 높이가 모두 같을 경우 경사로를 놓을 수 있다.
                # 경사로를 놓은 칸을 저장한다. (copy_row)
                if row[j + 1 : j + L + 1].count(row[j + 1]) == L:
                    for col in range(j + 1, j + L + 1):
                        copy_row[col] = -1
                    j += L
                else:
                    is_road = False
                    break

            # 다음 칸이 더 높을 때
            elif row[j] < row[j + 1]:
                # 경사로를 놓아도 범위를 벗어나는 경우 - 길이 없음
                if j + 1 - L < 0:
                    is_road = False
                    break

                # 경사로를 놓을 칸들의 높이가 모두 같을 경우
                # And
                # 그 자리에 이미 경사로가 놓여있지 않을 경우
                # 경사로를 놓을 수 있다.
                # 경사로를 놓은 칸을 저장한다. (copy_row)
                if (
                    row[j + 1 - L : j + 1].count(row[j]) == L
                    and copy_row[j + 1 - L : j + 1].count(-1) == 0
                ):
                    for col in range(j + 1 - L, j + 1):
                        copy_row[col] = -1
                    j += 1
                else:
                    is_road = False
                    break

        if is_road:
            cnt += 1

    return cnt


res += road_cnt()

# Transpose
for i in range(N):
    for j in range(i, N):
        _map[i][j], _map[j][i] = _map[j][i], _map[i][j]


res += road_cnt()
print(res)
