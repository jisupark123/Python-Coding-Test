# 다이얼

dial_chars = {
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ",
}

words = input()

res = 0

for w in words:
    for d in dial_chars:
        if w in dial_chars[d]:
            res += d + 1
            break

print(res)
