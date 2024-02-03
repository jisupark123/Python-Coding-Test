# 크게 만들기

"""
stack을 이용
1. k가 0이라면 push (k -> 지울 수 있는 횟수)
2. stack에 숫자가 없으면 push.
3. stack의 마지막 숫자가 넣으려는 숫자보다 같거나 높으면 push
4. stack의 마지막 숫자가 넣으려는 숫자보다 낮으면 pop, k-=1 -> 1번
5. 마지막에 남은 k만큼 뒤의 숫자를 지워준다.
"""

n, k = map(int, input().split())

nums = list(map(int, list(input().strip())))


stack = []

for num in nums:
    while True:
        if k == 0 or len(stack) == 0 or stack[-1] >= num:
            stack.append(num)
            break

        stack.pop()
        k -= 1

stack = stack[: len(stack) - k]

print("".join(map(str, stack)))
