# 숫자 야구

from sys import stdin


input = stdin.readline


def is_possible(num):
    def possible(num1, num2, condition: tuple):
        strike = 0
        ball = 0
        for i in range(3):
            if num1[i] == num2[i]:
                strike += 1
            elif num2[i] in num1:
                ball += 1
        if strike == condition[0] and ball == condition[1]:
            return True
        else:
            return False

    for q in questions:
        if not possible(str(num), str(q[0]), (q[1], q[2])):
            return False

    return True


N = int(input())

questions = [tuple(map(int, input().split())) for _ in range(N)]
res = 0

for num in range(123, 988):
    if len(set(str(num))) != 3 or "0" in str(num):
        continue
    if is_possible(num):
        res += 1

print(res)
