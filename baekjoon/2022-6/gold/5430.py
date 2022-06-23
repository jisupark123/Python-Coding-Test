# AC

from collections import deque
from sys import stdin


input = stdin.readline


def print_deque(deq):
    if len(deq) == 0:
        print([])
    else:
        res = "["
        for i in range(len(deq) - 1):
            res += f"{deq[i]},"
        res += f"{deq[-1]}]"
        print(res)


T = int(input())

for _ in range(T):
    functions = input().rstrip()
    functions = functions.replace("RR", "")  # 연속으로 두번 나오는 'R'을 없애준다
    cnt = int(input())
    lst = input().rstrip()
    if len(lst) == 2:  # []
        if "D" in functions:
            print("error")
        else:
            print([])
        continue
    lst = map(int, lst[1:-1].split(","))
    deq = deque(lst)

    reversing = False
    for f in functions:
        if f == "R":
            reversing = not reversing
        else:
            if len(deq) == 0:
                print("error")
                break
            if reversing:
                deq.pop()
            else:
                deq.popleft()
    else:
        if reversing:
            deq.reverse()
        print_deque(deq)
