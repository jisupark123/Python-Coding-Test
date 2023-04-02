# Hashing


def hashing(s: str) -> int:
    R = 31
    res = 0
    for i in range(len(s)):
        ascii_s = ord(s[i]) - 96
        r = R**i
        res += ascii_s * r
    return res


M = 1234567891

l = int(input())
s = input().strip()
print(hashing(s) % M)
