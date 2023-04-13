# 이중 우선순위 큐

import sys
import heapq

input = sys.stdin.readline

max_heap = []
min_heap = []

count = {}


def append(n):
    heapq.heappush(max_heap, -n)
    heapq.heappush(min_heap, n)
    if n in count:
        count[n] += 1
    else:
        count[n] = 1


def pop(type):
    if type == "max":
        while max_heap:
            item = -heapq.heappop(max_heap)
            if count[item] > 0:
                count[item] -= 1
                return
    else:
        while min_heap:
            item = heapq.heappop(min_heap)
            if count[item] > 0:
                count[item] -= 1
                return


def print_res():
    is_empty = True
    while max_heap:
        item = -heapq.heappop(max_heap)
        if count[item] > 0:
            print(item, end=" ")
            is_empty = False
            break
    if is_empty:
        print("EMPTY")
        return

    while min_heap:
        item = heapq.heappop(min_heap)
        if count[item] > 0:
            print(item)
            break


for _ in range(int(input())):
    for _ in range(int(input())):
        cmd, n = input().strip().split()
        if cmd == "I":
            append(int(n))
        else:
            pop("max" if n == "1" else "min")

    print_res()

    max_heap = []
    min_heap = []
    count = {}
