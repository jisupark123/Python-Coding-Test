# 쿼드트리

import sys

input = sys.stdin.readline

N = int(input())
video = [list(map(int, list(input().strip()))) for _ in range(N)]

# (0000) -> 0
def a(start_row, start_col, n):
    if n == 1:
        return str(video[start_row][start_col])
    res = ""
    res += a(start_row, start_col, n // 2)
    res += a(start_row, start_col + n // 2, n // 2)
    res += a(start_row + n // 2, start_col, n // 2)
    res += a(start_row + n // 2, start_col + n // 2, n // 2)
    if res == "0000":
        return "0"
    if res == "1111":
        return "1"
    else:
        return f"({res})"


print(a(0, 0, N))
