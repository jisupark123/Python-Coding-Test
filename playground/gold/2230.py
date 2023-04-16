# 수 고르기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [int(input()) for _ in range(N)]
lst.sort()

res = sys.maxsize

# 차이가 M이랑 같으면 출력 후 프로그램 종료
# 차이가 M보다 크면 res 갱신 후 break

left, right = 0, 1

while left < N and right < N:
    calc = lst[right] - lst[left]
    if calc == M:
        print(calc)
        exit(0)
    if calc < M:
        right += 1
        continue
    left += 1
    res = min(res, calc)

print(res)
