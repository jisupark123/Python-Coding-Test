# 지능형 기차 2

import sys

input = sys.stdin.readline

get_out = []
get_in = []
passengers = [0]

for _ in range(10):
    get_out, get_in = map(int, input().split())
    passengers.append(passengers[-1] - get_out + get_in)

print(max(passengers))
