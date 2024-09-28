# 숨바꼭질 5

"""
ans -> 동생을 찾는 가장 빠른 시간을 저장할 변수

visited 배열 -> 방문 처리를 위한 배열 (제자리로 돌아올 수 있다는 점을 방지하기 위함 -> 따라서 짝수시간/홀수시간 의 기록을 따로 해주어야 함)
- visited[n][0] -> 좌표 n에 도착한 시간중 가장 빠른 시간 (단, 시간이 짝수일 때)
- visited[n][1] -> 좌표 n에 도착한 시간중 가장 빠른 시간 (단, 시간이 홀수일 때)

동생이 좌표 n으로 움직이는 t시점에 다음을 수행
- visited[n]에 방문한 적이 있는지 확인 (n이 짝수면 visited[n][0], 홀수면 visited[n][1])
- 방문한 적이 있다면 t 출력 후 프로그램 종료
"""

import sys
from collections import deque

input = sys.stdin.readline

is_odd = lambda x: 0 if x % 2 == 0 else 1

x, target = map(int, input().split())

time = 0
target_speed = 1

q = deque()
q.append((x, 0))

visited = [[-1] * 2 for _ in range(500001)]
visited[x][0] = 0

while True:
    x, t = q.popleft()
    if t > time:
        time = t
        target += target_speed
        target_speed += 1

        if target > 500000:
            break

        if visited[target][is_odd(time)] != -1:
            print(time)
            exit(0)

    if x == target:
        print(time)
        exit(0)

    if x - 1 >= 0 and visited[x - 1][is_odd(t + 1)] == -1:
        visited[x - 1][is_odd(t + 1)] = 1
        q.append((x - 1, t + 1))

    if x + 1 <= 500000 and visited[x + 1][is_odd(t + 1)] == -1:
        visited[x + 1][is_odd(t + 1)] = 1
        q.append((x + 1, t + 1))

    if x * 2 <= 500000 and visited[x * 2][is_odd(t + 1)] == -1:
        visited[x * 2][is_odd(t + 1)] = 1
        q.append((x * 2, t + 1))

print(-1)
