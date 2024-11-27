# 세 용액

"""
숫자 1개 고르고 나머지 두개는 두 포인터로 search

O(n) x O(n)

리스트(nums) 정렬 후 모든 i에 대해 다음을 반복

1. 맨앞과 맨뒤에 포인터 a,b를 위치
2. nums[i] + nums[a] + nums[b]가 0보다 크면 b-=1, 0보다 작으면 a+=1
3. 이때 a나 b가 i와 겹치면 한칸 더 이동
"""


import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
nums.sort()

ans_num = sys.maxsize
comb = None

for a in range(n):
    i, j = 0, n - 1
    if i == a:
        i += 1
    elif j == a:
        j -= 1

    while i < j:

        total = nums[a] + nums[i] + nums[j]
        if abs(total) < ans_num:
            ans_num = abs(total)
            comb = [a, i, j]

        if total > 0:
            j -= 1
        elif total < 0:
            i += 1
        else:
            break

        if i == a:
            i += 1
        elif j == a:
            j -= 1

print(*sorted([nums[x] for x in comb]))
