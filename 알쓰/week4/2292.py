# 벌집

"""
4 -> 1
13 -> 2
28 -> 3
50 -> 4

1 6 12 18 24 30
"""

n = int(input())
b = 1
cnt = 1
while n > b:
    b += 6 * cnt
    cnt += 1
print(cnt)
