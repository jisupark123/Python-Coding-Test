# 숫자 카드 2


# def count_in_list(n, lst: list):
#     def count_num(i):
#         origin_idx = i
#         cnt = 1
#         while True:
#             i += 1
#             if i >= len(lst) or lst[i] != n:
#                 break
#             cnt += 1
#         i = origin_idx
#         while True:
#             i -= 1
#             if i < 0 or lst[i] != n:
#                 break
#             cnt += 1
#         return cnt

#     start = 0
#     end = len(lst) - 1
#     mid = (start + end) // 2

#     while start <= end:
#         if lst[mid] == n:
#             return count_num(mid)
#         elif lst[mid] > n:
#             end = mid - 1
#         else:
#             start = mid + 1
#         mid = (start + end) // 2

#     return 0


M = int(input())
cards = list(map(int, input().split()))
N = int(input())
nums = list(map(int, input().split()))


count = {}
for card in cards:
    try:
        count[card] += 1
    except:
        count[card] = 1


for num in nums:
    try:
        print(count[num], end=" ")
    except:
        print(0, end=" ")
