# 주사위 세개

dices = list(map(int, input().split()))


if len(set(dices)) == 1:
    print(10000 + (dices[0] * 1000))
elif len(set(dices)) == 2:
    for n in dices:
        if dices.count(n) == 2:
            num = n
            break
    print(1000 + (num * 100))

else:
    print(max(dices) * 100)
