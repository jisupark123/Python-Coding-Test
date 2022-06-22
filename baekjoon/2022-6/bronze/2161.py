# 카드1


from collections import deque

N = int(input())
q = deque(range(1, N + 1))

while len(q) > 1:
    print(q.popleft(), end=" ")
    q.append(q.popleft())

print(q[0])
