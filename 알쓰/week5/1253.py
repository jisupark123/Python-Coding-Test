# 좋다

"""
0이 하나 있으면 중복되는 숫자만큼 count 해주면 됨
0이 두개 있으면 
"""

N = int(input())

lst = list(map(int, input().split()))

s = set()

for i in range(N):
    for j in range(i + 1, N):
        if lst[i] != 0 and lst[j] == 0:
            s.add(lst[i] + lst[j])


cnt = 0

for i in range(N):
    if lst[i] in s:
        cnt += 1


print(cnt)
