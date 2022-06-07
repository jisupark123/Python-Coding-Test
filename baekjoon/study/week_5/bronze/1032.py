# 명령 프롬프트

import sys

input = sys.stdin.readline

N = int(input())
search_res = [input().strip() for _ in range(N)]

keyword = ""

for i in range(len(search_res[0])):
    s = search_res[0][i]
    same = True
    for j in search_res:
        if j[i] != s:
            same = False
            break

    if same:
        keyword += s
    else:
        keyword += "?"

print(keyword)
