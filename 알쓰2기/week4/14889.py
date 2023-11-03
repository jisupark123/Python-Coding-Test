import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

res = 1e9


combies = list(combinations(range(N), N // 2))
for combi in combies[: len(combies) // 2]:
    group1 = combi
    group2 = tuple(set(range(N)) - set(group1))

    power1 = sum(
        [
            sum(
                [
                    S[group1[a]][group1[b]] + S[group1[b]][group1[a]]
                    for b in range(len(combi))
                ]
            )
            for a in range(len(combi))
        ]
    )
    power2 = sum(
        [
            sum(
                [
                    S[group2[a]][group2[b]] + S[group2[b]][group2[a]]
                    for b in range(len(combi))
                ]
            )
            for a in range(len(combi))
        ]
    )
    res = min(res, abs(power1 - power2) // 2)

print(res)
