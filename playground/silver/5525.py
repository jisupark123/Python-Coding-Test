# IOIOI

import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().rstrip()
left, right = 0, 0
answer = 0

while right < M:
    if S[right : right + 3] == "IOI":
        right += 2
        if right - left == 2 * N:
            answer += 1
            left += 2
    else:
        left = right = right + 1

print(answer)
