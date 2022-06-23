# 스위치 켜고 끄기

from sys import stdin


input = stdin.readline


def man(num):
    origin_num = num
    global switches
    while True:
        try:
            switches[num] = 0 if switches[num] == 1 else 1
            num += origin_num
        except:
            return


def woman(num):
    global switches
    start = end = num
    switches[num] = 0 if switches[num] == 1 else 1
    while True:
        try:
            if switches[start - 1] == switches[end + 1]:
                switches[start - 1] = 0 if switches[start - 1] == 1 else 1
                switches[end + 1] = 0 if switches[end + 1] == 1 else 1
                start -= 1
                end += 1
            else:
                return
        except:
            return


switch_cnt = int(input())
switches_lst = list(map(int, input().split()))
switches = {}
for i in range(1, switch_cnt + 1):
    switches[i] = switches_lst[i - 1]

student_cnt = int(input())
for _ in range(student_cnt):
    gender, num = map(int, input().split())
    if gender == 1:
        man(num)
    else:
        woman(num)

for i, value in enumerate(switches.values()):
    print(value, end=" ")
    if (i + 1) % 20 == 0:
        print()
