# 다각형의 면적

import math
import sys

input = sys.stdin.readline

N = int(input())
x_lst = []
y_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

x_lst.append(x_lst[0])
y_lst.append(y_lst[0])

res = 0

a = 0
b = 0

for i in range(len(x_lst) - 1):
    a += x_lst[i] * y_lst[i + 1]

for i in range(len(y_lst) - 1):
    a += y_lst[i] * x_lst[i + 1]

res = math.fabs(0.5 * (a - b))
print("%.1f" % res)
