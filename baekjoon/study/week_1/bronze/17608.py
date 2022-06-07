# 막대기

import sys

num_of_stick = int(sys.stdin.readline())
sticks = []
for _ in range(num_of_stick):
    sticks.append(int(sys.stdin.readline()))

tallest_stick = 0
result = 1
tallest_stick = sticks[-1]

for i in range(num_of_stick - 2, -1, -1):
    if sticks[i] > tallest_stick:
        result += 1
        tallest_stick = sticks[i]
print(result)
