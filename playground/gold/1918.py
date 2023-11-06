"""
1. 피연산자 -> result에 넣는다.
2. ( -> stack에 push()
3. ) -> (가 나올 때까지 스택에서 pop()하고 모두 result에 넣는다.
4. 연산자(좌괄호 포함) -> 스택에 있는 연산자와 비교한다. 
4-1. 스택이 비어있거나 연산자의 우선 순위가 높다면 스택에 push()하고 처음으로 돌아간다.
4-2. 스택에 있는 연산자의 우선 순위가 높거나 같다면 스택.pop()해서 result에 넣고 2번으로 돌아간다.
5. 순회가 끝나면 스택에서 pop()하고 모두 result에 넣는다.

"""


S = input().strip()

rank = {
    "(": 0,
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}

res = ""
stack = []
for s in S:
    # 1. 피연산자 -> result에 넣는다.
    if s not in ("(", ")", "+", "-", "*", "/"):
        res += s

    # 2. ( -> stack에 push()
    elif s == "(":
        stack.append(s)
    # 3. ) -> (가 나올 때까지 스택에서 pop()하고 모두 result에 넣는다.
    elif s == ")":
        # i = stack[::-1].index("(") + 1
        for _ in range(len(stack)):
            op = stack.pop()
            if op == "(":
                break
            res += op

    # 4. 연산자(좌괄호 포함) -> 스택에 있는 연산자와 비교한다.
    # 4-1. 스택이 비어있거나 연산자의 우선 순위가 높다면 스택에 push()하고 처음으로 돌아간다.
    # 4-2. 스택에 있는 연산자의 우선 순위가 높거나 같다면 스택.pop()해서 result에 넣고 3번으로 돌아간다.
    else:
        while True:
            if len(stack) == 0 or rank[s] > rank[stack[-1]]:
                stack.append(s)
                break
            else:
                res += stack.pop()

# 5. 순회가 끝나면 스택에서 pop()하고 모두 result에 넣는다.
res += "".join(stack[::-1])

print(res)
