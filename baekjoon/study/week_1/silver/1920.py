# 수 찾기

import sys

input = sys.stdin.readline

N = int(input())
A = set(input().split())
M = int(input())
X = input().split()

for x in X:
    if x in A:
        print(1)
    else:
        print(0)
