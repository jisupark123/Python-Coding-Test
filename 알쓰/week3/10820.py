# 문자열 분석

import sys

input = sys.stdin.readline

while True:
    try:
        lower, upper, number, blank = 0, 0, 0, 0
        string = input().rstrip()
        for s in string:
            if s == " ":
                blank += 1
            elif s in map(str, range(10)):
                number += 1
            elif s == s.lower():
                lower += 1
            else:
                upper += 1
        print(f"{lower} {upper} {number} {blank}")

    except EOFError:
        break
