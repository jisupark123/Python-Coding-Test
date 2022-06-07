# 나무 자르기

import sys

input = sys.stdin.readline

tree_cnt, target = map(int, input().split())
trees = list(map(int, input().split()))


def upDown(nums, target, guess):
    res = 0
    for num in nums:
        if num > guess:
            res += num - guess
    if res >= target:
        return "up"
    else:
        return "down"


def cut_tree(trees, target):
    max_range = max(trees)
    min_range = 1
    while min_range <= max_range:
        point = (max_range + min_range) // 2
        res = upDown(trees, target, point)
        if res == "up":
            min_range = point + 1
        elif res == "down":
            max_range = point - 1

    return max_range


print(cut_tree(trees, target))
