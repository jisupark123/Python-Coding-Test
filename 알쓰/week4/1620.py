# 나는야 포켓몬 마스터 이다솜

import sys

input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())

n_to_p = {}
p_to_n = {}

for i in range(1, N + 1):
    name = input()
    n_to_p[i] = name
    p_to_n[name] = i

for _ in range(M):
    key = input()
    try:
        print(n_to_p[int(key)])
    except:
        print(p_to_n[key])
