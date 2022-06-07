# 암기왕

import sys


def a_in_b(a, b):
    start = 0
    end = len(b)
    while True:
        pointer = (start + end) // 2
        if end - start < 5:
            return a in b[start:end]
        if a > b[pointer]:
            start = pointer + 1
        elif a < b[pointer]:
            end = pointer
        else:
            return True


input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = input()
    note_1 = list(map(int, input().split()))
    note_1 = sorted(set(note_1))
    M = input()
    note_2 = list(map(int, input().split()))
    for i in note_2:
        if a_in_b(i, note_1):
            print(1)
        else:
            print(0)
