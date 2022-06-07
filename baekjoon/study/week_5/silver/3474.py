# 교수가 된 현우

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())  # 수 입력 받기
    count = 0
    i = 5
    while i <= n:
        count += n // i  # 5의 배수의 합을 구한다
        i *= 5
    print(count)
