# A와 B

import sys


S = input()
T = input()


def op1(s):  # 연산1: 문자열의 뒤에 A를 추가한다.
    return s + "A"


def op2(s):  # 연산2: 문자열을 뒤집고 뒤에 B를 추가한다.
    return s[::-1] + "B"


def dfs(s):
    if s == T:
        print(1)
        sys.exit()
    if len(s) >= len(T):
        return

    dfs(op1(s))
    dfs(op2(s))


dfs(S)
print(0)
