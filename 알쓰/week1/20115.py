# 에너지 드링크

N = int(input())
drinks = list(map(int, input().split()))
max_drink = max(drinks)

res = sum(map(lambda x: x / 2, drinks)) + (max_drink / 2)
print(int(res) if int(res) == res else res)
