"""
1. 각 배열의 누적합 구하기
2. 나올 수 있는 모든 부배열 조합의 합을 각각 구하기 (lst1_all_combi, lst2_all_combi)
3. lst2_all_combi를 돌면서 각 숫자의 개수를 count
4. lst1_all_combi를 돌면서 T - 숫자의 값이 위에서 구한 count에 있는지 확인
"""

import sys
from collections import defaultdict

input = sys.stdin.readline


# a에서 b까지 구간합 구하기
def part_sum(a, b, lst_accsum):
    if a == 0:
        return lst_accsum[b]
    return lst_accsum[b] - lst_accsum[a - 1]


def all_combi(lst, lst_accsum):
    res = []
    for a in range(len(lst)):
        for b in range(a, len(lst)):
            res.append(part_sum(a, b, lst_accsum))
    return res


T = int(input())
n = int(input())
lst1 = list(map(int, input().split()))
m = int(input())
lst2 = list(map(int, input().split()))

lst1_accsum = lst1[:]  # lst1 누적합
for i in range(1, n):
    lst1_accsum[i] += lst1_accsum[i - 1]

lst2_accsum = lst2[:]  # lst2 누적합
for i in range(1, m):
    lst2_accsum[i] += lst2_accsum[i - 1]

lst1_all_combi = all_combi(lst1, lst1_accsum)
lst2_all_combi = all_combi(lst2, lst2_accsum)

lst1_all_combi.sort()
lst2_all_combi.sort()

ans = 0

cnt_dict = defaultdict(int)

for num in lst2_all_combi:
    cnt_dict[num] += 1

for num in lst1_all_combi:
    ans += cnt_dict[T - num]


print(ans)
