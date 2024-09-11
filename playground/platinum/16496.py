# 큰 수 만들기

import sys
from functools import cmp_to_key

input = sys.stdin.readline


def sort_fn(a, b):

    if a + b > b + a:
        return 1
    return -1


N = int(input())

nums = list(input().strip().split())


nums.sort(key=cmp_to_key(sort_fn), reverse=True)

print(0 if nums[0] == "0" else "".join(nums))
