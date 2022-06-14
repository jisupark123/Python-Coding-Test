# 그룹 단어 체커

import sys


input = sys.stdin.readline


def is_group_word(word):
    word = "0" + word
    pre_words = []
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            continue
        if word[i] not in pre_words:
            pre_words.append(word[i])
        else:
            return False
    return True


N = int(input())
res = 0
for _ in range(N):
    word = input().strip()
    if is_group_word(word):
        res += 1

print(res)
