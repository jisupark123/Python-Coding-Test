import sys

input = sys.stdin.readline

N = int(input())

players = [input().strip() for _ in range(N)]
res = []

for s in map(lambda x: x[0], players):
    if s not in res and len(list(filter(lambda x: x[0] == s, players))) >= 5:
        res.append(s)

if len(res):
    print("".join(sorted(res)))
else:
    print("PREDAJA")
