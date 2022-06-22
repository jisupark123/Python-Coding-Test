# 완전제곱수

import math


M = int(input())
N = int(input())

res = []
for num in range(M, N + 1):
    if math.sqrt(num) == int(math.sqrt(num)):
        res.append(num)

if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
