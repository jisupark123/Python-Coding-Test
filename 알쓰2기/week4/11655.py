S = input()

res = ""

for s in S:
    if not (ord("a") <= ord(s) <= ord("z")) and not (ord("A") <= ord(s) <= ord("Z")):
        res += s
        continue
    n = ord(s) + 13
    if s != s.lower():  # 대문자
        if n > ord("Z"):
            res += chr(n - 26)
        else:
            res += chr(n)
    else:
        if n > ord("z"):
            res += chr(n - 26)
        else:
            res += chr(n)

print(res)
