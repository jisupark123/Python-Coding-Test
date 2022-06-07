# 암호해독기

import sys

input = sys.stdin.readline

N = input()
password = list(map(int, input().split()))
s = input()

new_password = []

for i in s:
    if i.islower():
        new_password.append(ord(i) - 70)
    elif i.isupper():
        new_password.append(ord(i) - 64)
    elif i == " ":
        new_password.append(0)

if sorted(password) == sorted(new_password):
    print("y")
else:
    print("n")
