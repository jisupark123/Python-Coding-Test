# 비밀번호 찾기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())


pws = {}


for _ in range(N):
    site, pw = input().rstrip().split()
    pws[site] = pw

for _ in range(M):
    print(pws[input().rstrip()])
