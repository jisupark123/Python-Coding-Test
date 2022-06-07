# 폴리오미노


def polyomino():
    board = input() + "."
    res = ""

    block_A = "AAAA"
    block_B = "BB"

    cnt = 0
    for b in board:
        if b == "X":
            cnt += 1
        elif cnt == 0:
            res += "."
        else:
            if cnt % 2 == 0:
                a = cnt // 4
                b = (cnt - 4 * a) // 2
                res += block_A * a
                res += block_B * b
                cnt = 0
                res += "."
            else:
                return -1
    return res[:-1]


print(polyomino())
