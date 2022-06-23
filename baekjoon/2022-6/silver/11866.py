# 요세푸스 문제 0

from collections import deque


N, K = map(int, input().split())

people = deque(range(1, N + 1))
res = "<"

while people:

    for _ in range(K - 1):
        people.append(people.popleft())

    res += f"{people.popleft()}"

    if people:
        res += ", "

print(res + ">")
