# 잃어버린 괄호

import sys

input = sys.stdin.readline

lst = []
a = ""
for s in input().strip():
    if s == "-":
        lst.append(a)
        a = ""
    else:
        a += s

lst.append(a)


def parse(p):
    res = 0
    r = ""
    for s in p:
        if s == "+":
            res += int(r)
            r = ""
        else:
            r += s
    if len(r):
        res += int(r)
    return res


res = parse(lst[0])
for n in lst[1:]:
    res -= parse(n)

print(res)
