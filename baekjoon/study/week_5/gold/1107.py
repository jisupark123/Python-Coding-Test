# 리모컨

import sys

input = sys.stdin.readline

target_chanel = int(input())
M = int(input())

broken_btns = list(map(int, input().split()))
available_btns = [x for x in range(10) if x not in broken_btns]

start_chanel = 100
curr_chanel = start_chanel

