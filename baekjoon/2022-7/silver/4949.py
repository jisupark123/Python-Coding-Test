# 균형잡힌 세상

from sys import stdin


input = stdin.readline


def is_balance(sentence: str) -> bool:
    stack = []
    for s in sentence:
        if s in ["(", "["]:
            stack.append(s)
        elif s in [")", "]"]:
            if len(stack) == 0:
                return False
            a = stack.pop()
            if (a == "(" and s == "]") or (a == "[" and s == ")"):
                return False

    if len(stack) == 0:
        return True
    else:
        return False


while True:
    sentence = input().rstrip()
    if (sentence) == ".":
        break
    if is_balance(sentence):
        print("yes")
    else:
        print("no")
