import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))


stack = []
res = []
for num in nums[::-1]:
    while stack:
        if num >= stack[-1]:
            stack.pop()
        else:
            break
    if len(stack) == 0:
        res.append(-1)
    else:
        res.append(stack[-1])
    stack.append(num)

print(*res[::-1])
