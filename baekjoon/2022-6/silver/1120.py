# 문자열


def gap_of_ab(a, b):
    res = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            res += 1
    return res


a, b = input().strip().split()

min_gap = len(b)


for i in range(len(b) - len(a) + 1):
    min_gap = min(gap_of_ab(a, b[i : len(b)]), min_gap)

print(min_gap)
