# 복권

from itertools import combinations


N, M, K = map(int, input().split())

combies = list(combinations(range(1, N + 1), M))

count = 0

for a in combies:
    for b in combies:
        if abs(len(set(a) - set(b))):
            count += 1
print(count / len(combies))
