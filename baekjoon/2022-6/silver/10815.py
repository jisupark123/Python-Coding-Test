# 숫자 카드


def num_in_cards(num):
    start = 0
    end = len(cards) - 1
    while True:
        mid = (start + end) // 2
        if cards[mid] == num:
            return True
        if start >= end:
            return False
        if cards[mid] > num:
            end = mid - 1
        else:
            start = mid + 1


N = input()
cards = list(map(int, input().split()))
cards.sort()
M = input()
nums = list(map(int, input().split()))
for num in nums:
    if num_in_cards(num):
        print(1, end=" ")
    else:
        print(0, end=" ")
