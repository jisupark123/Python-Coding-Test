# 생일

from sys import stdin


input = stdin.readline

n = int(input())

students = [input().strip().split(" ") for _ in range(n)]
students.sort(key=lambda x: (x[3]))
students.sort(key=lambda x: (x[2], x[1]), reverse=True)
print(students)
