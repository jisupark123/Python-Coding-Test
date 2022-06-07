# 단어 나누기

s = input()
res = "z" * 100

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s)):
        new_word = s[:i][::-1] + s[i:j][::-1] + s[j:][::-1]
        if new_word < res:
            res = new_word

print(res)
