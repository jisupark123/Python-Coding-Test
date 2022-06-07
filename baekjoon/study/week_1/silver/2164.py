# 카드2

# n = int(input())

# cards = [x for x in range(1, n + 1)]
# answer = []
# while len(cards) > 1:
#     cards = cards[2:] + [cards[1]]
# print(cards[0])

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])
while len(deque) > 1:
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])


# input = int(input())
# square = 2
# while True:
#     if input == 1 or input == 2:
#         print(input)
#         break
#     square *= 2
#     if square >= input:
#         print((input - (square // 2)) * 2)
#         break
