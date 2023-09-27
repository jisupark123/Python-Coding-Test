# 유레카 이론

import sys

input = sys.stdin.readline

triangle_nums = [1]

for i in range(2, 1000):
    triangle_nums.append(triangle_nums[-1] + i)
    if triangle_nums[-1] >= 1000:
        break


for _ in range(int(input())):
    n = int(input())
    t_nums = list(filter(lambda x: x < n, triangle_nums))
    flag = False
    for a in range(len(t_nums)):
        if flag:
            break
        for b in range(len(t_nums)):
            if flag:
                break
            for c in range(len(t_nums)):
                if t_nums[a] + t_nums[b] + t_nums[c] == n:
                    flag = True
                    break

    if flag:
        print(1)
    else:
        print(0)
