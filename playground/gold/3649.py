# 로봇 프로젝트

"""
1 2 98 99
x -> 구멍의 너비
i -> 0, j -> n-1

ans_i = -1 (정답 i)
ans_j = -1 (정답 j)

반복문으로 i와 j를 서서히 좁혀나간다.
i가 j와 같아지면 반복문 종료, danger 출력

legos[i] + legos[j] == x 이면 i, j 출력 후 break
legos[i] + legos[j] > x 이면 j -= 1 (크기를 줄여야됨)
legos[i] + legos[j] < x 이면 i += 1 (크기를 늘려야됨)
"""

import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 1e7
        n = int(input())
        legos = sorted([int(input()) for _ in range(n)])

        i = 0
        j = n - 1
        ans = False

        while i < j:
            tmp = legos[i] + legos[j]
            if tmp == x:
                print("yes", legos[i], legos[j])
                ans = True
                break
            if tmp > x:
                j -= 1
            else:
                i += 1
        if not ans:
            print("danger")

    except:
        break
