# 블랙잭
from itertools import combinations


N, target_number = map(int, input().split())

cards = list(map(int, input().split()))
combies = list(combinations(cards, 3))

gap = target_number

for combi in combies:
    sum_combi = sum(combi)
    if sum_combi > target_number or target_number - sum_combi >= gap:
        continue
    else:
        gap = target_number - sum_combi

print(target_number - gap)
