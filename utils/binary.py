# 소수가 포함된 2진수를 10진수로 변환
def float_bin_to_oct(num):
    int_part, float_part = str(num).split(".")
    float_part = int(float_part) / (int("1" + "0" * len(float_part)))
    res = format(int(int_part), "b") + "."
    while float_part != 0:
        float_part *= 2
        res += str(int(float_part))
        float_part -= int(float_part)
    return float(res)


# 소수가 포함된 10진수를 2진수로 변환
def float_oct_to_bin(num):
    res = 0
    square = len(str(int(num))) - 1
    for n in str(num):
        if n == ".":
            continue
        res += 2**square * int(n)
        print(res)
        square -= 1
    return res
