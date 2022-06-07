# 도로와 신호등

import sys

input = sys.stdin.readline

N, L = map(int, input().split())  # 신호등의 개수 N과 도로의 길이 L

signal_lights = [tuple(map(int, input().split())) for _ in range(N)]

current_pos = 0  # 현재 포지션
elapsed_times = 0  # 경과 시간

for light in signal_lights:
    elapsed_times += light[0] - current_pos
    current_pos = light[0]
    time_to_wait = light[1] - (elapsed_times % (light[1] + light[2]))
    if 0 < time_to_wait:
        elapsed_times += time_to_wait

elapsed_times += L - current_pos
print(elapsed_times)
