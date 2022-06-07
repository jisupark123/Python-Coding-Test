# 토너먼트

import sys


def next_num(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num // 2 + 1


input = sys.stdin.readline

N, Kim, Lim = map(int, input().split())

round = 1
while True:
    Kim, Lim = next_num(Kim), next_num(Lim)
    if Kim == Lim:
        print(round)
        break
    else:
        round += 1
