# 셀프 넘버


def d(n):
    temp = list(str(n))
    temp = sum(map(int, temp))
    return n + temp


self_nums = [True] * 10001  # 1부터 10000까지

for i in range(1, 10001):
    try:
        self_nums[d(i)] = False
    except:
        continue

for i in range(1, len(self_nums)):
    if self_nums[i] == True:
        print(i)
