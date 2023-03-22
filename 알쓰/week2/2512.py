# 예산

import sys

input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
total_money = int(input())


def is_possible(top):
    def func(num):
        if num <= top:
            return num
        else:
            return top

    _sum = sum(map(func, req))
    return True if _sum <= total_money else False


if sum(req) <= total_money:
    print(max(req))
else:
    start = 0
    end = total_money
    mid = (start + end) // 2
    while mid < end:
        if is_possible(mid):
            if not is_possible(mid + 1):
                print(mid)
                break
            else:
                start = mid
                mid = (start + end) // 2
        else:
            if is_possible(mid - 1):
                print(mid - 1)
                break
            else:
                end = mid
                mid = (start + end) // 2
