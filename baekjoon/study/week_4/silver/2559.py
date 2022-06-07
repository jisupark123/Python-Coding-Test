# 수열

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

temp = list(map(int, input().split()))

# max_temp = 0
# temps = []
# for i in range(0, N - K + 1):
#     temps.append(sum(temp[i : i + K]))

# print(max(temps))

part_sum = sum(temp[:K])
result_list = [part_sum]

for i in range(0, len(temp) - K):
    part_sum = part_sum - temp[i] + temp[i + K]
    result_list.append(part_sum)

print(max(result_list))
