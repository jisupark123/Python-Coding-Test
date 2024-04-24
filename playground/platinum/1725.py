# 히스토그램

"""
- 스택 사용
- 높이가 변경될 때 이전에 저장한 높이를 통해 최대 너비 구하기
- 스택에 index와 number를 같이 저장 ([idx, num])

- 높이가 높아진다면 
-> 스택에 push

- 높이가 낮아진다면
1. 같거나 낮은 높이가 나올 때까지 pop + 최대 너비 갱신
2. 마지막으로 pop한 인덱스를 stack에 push | ex. [2]에서 1을 push하면 2를 삭제하고 2의 index와 숫자 1을 저장

- 같은 숫자가 연속으로 나올 것을 대비해서 list 마지막에 0을 넣어줌
"""

import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)] + [0]

stack = []  # idx, height
ans = 0


for i in range(N + 1):
    idx = i

    while stack and stack[-1][1] > nums[i]:
        idx, height = stack.pop()
        ans = max(ans, height * (i - idx))

    stack.append([idx, nums[i]])


print(ans)
