# 공 바꾸기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 공 -> 1 ~ N
balls = list(range(1, N + 1))

# 서로 교환할 공들 M개
# 인덱스는 0부터 시작하므로 각각 1씩 빼준다.
change = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]

# c -> (공1,공2)
# 교환할 공을 꺼내서 balls 리스트에서 교환한다.
for c in change:
    balls[c[0]], balls[c[1]] = balls[c[1]], balls[c[0]]

# 모두 바꾸고 난 다음 공 출력
for ball in balls:
    print(ball, end=" ")
