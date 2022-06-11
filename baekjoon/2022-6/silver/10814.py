# 나이순 정렬

import sys

input = sys.stdin.readline

N = int(input())
members = []

for _ in range(N):
    age, name = input().strip().split()
    members.append((int(age), name))

members.sort(key=lambda x: x[0])

for member in members:
    print(member[0], member[1])
