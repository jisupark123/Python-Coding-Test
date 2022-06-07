# 단어 수학

import sys

input = sys.stdin.readline

N = int(input())

# N개의 단어를 리스트에 저장
words = [input().strip() for _ in range(N)]

dic = {}  # 단어의 크기를 저장할 딕셔너리
nums = list(range(9, -1, -1))  # 9에서 0까지
res = 0

# 단어가 담긴 리스트를 순회하면서 딕셔너리에 크기를 저장
for word in words:
    for i in range(len(word)):
        try:
            dic[word[-(i + 1)]] += 10**i
        except:
            dic[word[-(i + 1)]] = 10**i

# 큰 값 -> 작은 값 순으로 정렬
lst = sorted([dic[x] for x in dic], reverse=True)

# 제일 큰 값부터 차례대로 곱해서 res에 더하기
for i in range(len(lst)):
    res += lst[i] * nums[i]

print(res)
