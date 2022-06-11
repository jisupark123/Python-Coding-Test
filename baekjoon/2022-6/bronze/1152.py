# 단어의 개수

s = input().strip()

lst = s.split(" ")
res = 0
for i in lst:
    if i != "":
        res += 1

print(res)
