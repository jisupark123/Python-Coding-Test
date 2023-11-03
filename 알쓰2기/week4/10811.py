import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [x for x in range(1, N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    for i, n in enumerate(reversed(lst[a - 1 : b])):
        lst[a - 1 + i] = n

print(*lst)
