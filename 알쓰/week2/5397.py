# 키로거
import sys
from collections import deque


def get_password(s: str) -> str:
    lst = deque()
    cursor = 0
    for key in s:
        if key == "<":
            if cursor > 0:
                cursor -= 1
        elif key == ">":
            if cursor < len(lst):
                cursor += 1
        elif key == "-":
            if cursor > 0:
                del lst[cursor - 1]
                cursor -= 1
        else:
            lst.insert(cursor, key)
            cursor += 1

    return "".join(lst)


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    s = input().strip()
    print(get_password(s))
