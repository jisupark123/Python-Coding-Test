# 트로피 진열

import sys

input = sys.stdin.readline
N = int(input())

lst = [int(input()) for _ in range(N)]


def solution(lst: list[int]) -> int:
    prev_num = 0
    res = 0
    for num in lst:
        if num > prev_num:
            res += 1
            prev_num = num

    return res


print(solution(lst))
print(solution(lst[::-1]))
