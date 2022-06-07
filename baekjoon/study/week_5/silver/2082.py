# 시계


numbers = {
    0: ("###" + "#.#" * 3 + "###"),
    1: ("..#" * 5),
    2: ("###..#####..###"),
    3: ("###..####..####"),
    4: ("#.#" * 2 + "###" + "..#" * 2),
    5: ("####..###..####"),
    6: ("####..####.####"),
    7: ("###" + "..#" * 4),
    8: ("####.#####.####"),
    9: ("####.####..####"),
}

t1, t2, t3, t4 = "", "", "", ""

for _ in range(5):
    a, b, c, d = input().strip().split()
    t1 += a
    t2 += b
    t3 += c
    t4 += d


res = ""

for t in (t1, t2, t3, t4):
    for n in numbers:
        can_fix = True
        for i in range(len(t1)):
            if t[i] == "#" and numbers[n][i] == ".":
                can_fix = False

        if can_fix == True:
            res += str(n)
            break


print(res[:2] + ":" + res[2:])
