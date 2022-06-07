# 회문

import sys

input = sys.stdin.readline

# 회문 판별 함수
def is_palindrome(s):
    middle = len(s) // 2 + 1
    return True if s[:middle] == s[-middle:][::-1] else False


def like_palindrome(s):
    len_s = len(s)
    for i in range(len_s // 2):
        if s[i] != s[(len_s - 1) - i]:
            if is_palindrome(s[:i] + s[i + 1 :]) or is_palindrome(
                s[: (len_s - 1) - i] + s[len_s - i :]
            ):
                return True
            else:
                return False


T = int(input())
sample = []

for _ in range(T):
    sample.append(input().strip())

for s in sample:
    if is_palindrome(s):
        print(0)
    elif like_palindrome(s):
        print(1)
    else:
        print(2)
