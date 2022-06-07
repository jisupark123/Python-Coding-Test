# 도영이가 만든 맛있는 음식

from itertools import combinations


N = int(input())
ingredients = [tuple(map(int, input().split())) for _ in range(N)]

min_gap = 1e9

for n in range(1, N + 1):

    for combi in list(combinations(range(N), n)):
        total_sourness = 1  # 신맛 총합 (재료들의 곱)
        total_bitterness = 0  # 쓴맛 총합 (재료들의 합)
        for c in combi:
            total_sourness *= ingredients[c][0]
            total_bitterness += ingredients[c][1]

        min_gap = min(abs(total_sourness - total_bitterness), min_gap)

print(min_gap)
