# 올림픽

import sys

input = sys.stdin.readline

N, K = map(int, input().split())  # N=국가 수 K=등수를 알고 싶은 국가

olympic_res = [list(map(int, input().split())) for _ in range(N)]
olympic_res.sort(key=lambda x: x[0])
K_res = olympic_res[K - 1]
rank = 1

for res in olympic_res:
    if res[1] > K_res[1]:
        rank += 1
    elif res[1] == K_res[1]:
        if res[2] > K_res[2]:
            rank += 1
        elif res[2] == K_res[2]:
            if res[3] > K_res[3]:
                rank += 1

print(rank)
