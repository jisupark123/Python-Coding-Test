# 트리 순회

import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    key, *children = list(input().strip().split())
    tree[key] = children


def front(key):
    if key == ".":
        return
    print(key, end="")
    front(tree[key][0])
    front(tree[key][1])


def middle(key):
    if key == ".":
        return
    middle(tree[key][0])
    print(key, end="")
    middle(tree[key][1])


def back(key):
    if key == ".":
        return
    back(tree[key][0])
    back(tree[key][1])
    print(key, end="")


front("A")
print()
middle("A")
print()
back("A")
