# 평행선

import sys
from collections import defaultdict

n = int(sys.stdin.readline())
x_dicts = defaultdict(list)
y_dicts = defaultdict(list)

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    x_dicts[a].append(b)
    y_dicts[b].append(a)

answer = 0
for key in x_dicts:
    if len(x_dicts[key]) >= 2:
        answer += 1
for key in y_dicts:
    if len(y_dicts[key]) >= 2:
        answer += 1

print(answer)
