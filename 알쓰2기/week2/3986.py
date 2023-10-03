import sys

input = sys.stdin.readline

n = int(input())

words = [input().strip() for _ in range(n)]


# ABBABB
def is_good_word(word):
    stack = []
    for w in word:
        if len(stack) == 0 or stack[-1] != w:
            stack.append(w)
        elif stack[-1] == w:
            stack.pop()

    if len(stack):
        return False
    return True


res = 0

for word in words:
    if is_good_word(word):
        res += 1

print(res)
