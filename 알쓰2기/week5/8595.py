# 히든 넘버


N = int(input())
S = input().strip()

tmp = ""
hidden_nums = []

for s in S:
    if s in "0123456789":
        tmp += s
    else:
        if len(tmp):
            hidden_nums.append(int(tmp))
            tmp = ""
if len(tmp):
    hidden_nums.append(int(tmp))

print(sum(hidden_nums))
