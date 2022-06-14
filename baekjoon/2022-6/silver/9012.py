# 괄호

import sys

input = sys.stdin.readline


def is_VPS(string):
    count = 0
    for s in string:
        if s == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


T = int(input())

for _ in range(T):
    s = input().strip()
    if is_VPS(s):
        print("YES")
    else:
        print("NO")
