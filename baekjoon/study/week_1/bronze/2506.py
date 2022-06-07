# 점수 계산

import sys

n = int(sys.stdin.readline())
res = list(map(int, input().split()))
answer = 0
combo = 0
for i in range(n):
    if res[i] == 1:
        answer += combo + 1
        combo += 1
    else:
        combo = 0
print(answer)
