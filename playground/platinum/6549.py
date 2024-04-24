# 히스토그램에서 가장 큰 직사각형

import sys

input = sys.stdin.readline

while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        break
    N = tmp[0]
    nums = tmp[1:] + [0]

    stack = []  # idx, height
    ans = 0

    for i in range(N + 1):
        idx = i

        while stack and stack[-1][1] > nums[i]:
            idx, height = stack.pop()
            ans = max(ans, height * (i - idx))

        stack.append([idx, nums[i]])

    print(ans)
