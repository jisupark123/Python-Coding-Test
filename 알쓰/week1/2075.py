# N번째 큰 수

import sys
import heapq

# sys.setrecursionlimit(10000000)

input = sys.stdin.readline

N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]


res = []
for _ in range(N):
    for num in map(int, input().split()):
        if len(res) < N:
            heapq.heappush(res, num)
        else:
            if num > res[0]:
                heapq.heappushpop(res, num)

print(res[-N])


# def merge(lst1, lst2):
#     new_lst = []
#     i1, i2 = 0, 0
#     while True:
#         if i1 == len(lst1):
#             new_lst.extend(lst2[i2:])
#             break
#         if i2 == len(lst2):
#             new_lst.extend(lst1[i1:])
#             break
#         if lst1[i1] < lst2[i2]:
#             new_lst.append(lst1[i1])
#             i1 += 1
#         else:
#             new_lst.append(lst2[i2])
#             i2 += 1
#     return new_lst


# for i in range(N):
#     res = merge(res, [lst[j][i] for j in range(N)])

# print(res[-N])
