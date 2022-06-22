# 크로아티아 알파벳

s = input()

alphabets = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]


def distinguish(s):
    if s in alphabets:
        return 2
    else:
        return 1


res = 0
i = 0
while i < len(s):
    try:
        if s[i : i + 3] == "dz=":
            idx_jump = 3
        else:
            idx_jump = distinguish(s[i : i + 2])
        i += idx_jump
    except:
        i += 1
    finally:
        res += 1

print(res)
