# 큐


from collections import deque
from sys import stdin

input = stdin.readline


class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, num):
        self.queue.append(num)

    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.queue.popleft()

    def front(self):
        if self.empty():
            return -1
        else:
            return self.queue[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.queue[-1]


N = int(input())
queue = Queue()

for _ in range(N):
    command = input().strip().split(" ")
    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "pop":
        print(queue.pop())
    elif command[0] == "size":
        print(queue.size())
    elif command[0] == "empty":
        print(queue.empty())
    elif command[0] == "front":
        print(queue.front())
    elif command[0] == "back":
        print(queue.back())
