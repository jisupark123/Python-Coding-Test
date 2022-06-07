# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
ice_cream = [[False for _ in range(N)] for _ in range(N)]
for i in range(M):
    i1, i2 = map(int, input().split())
    ice_cream[i1 - 1][i2 - 1] = True
    ice_cream[i2 - 1][i1 - 1] = True

answer = 0

for i in combinations(range(N), 3):
    if ice_cream[i[0]][i[1]] or ice_cream[i[0]][i[2]] or ice_cream[i[1]][i[2]]:
        continue
    answer += 1
print(answer)

# N, M = map(int, sys.stdin.readline().split())
# bad_combies = []
# for _ in range(M):
#     bad_combies.append(list(map(int, sys.stdin.readline().split())))

# answer = 0
# for combi in combinations(range(1, N + 1), 3):
#     is_ok = True
#     for bad_combi in bad_combies:
#         if len(set(combi) - set(bad_combi)) == 1:
#             is_ok = False
#             break
#     if is_ok:
#         answer += 1

# print(answer)

# 시간초과
