# 듣보잡

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

no_hear = [input().strip() for _ in range(N)]
no_see = [input().strip() for _ in range(M)]

res = sorted(set(no_hear) & set(no_see))

print(len(res))
for name in res:
    print(name)
