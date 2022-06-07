# 졸려


def shuffle_s(s):
    start = 1 if len(s) % 2 == 0 else 2
    for i in range(start, len(s), 2):
        temp = s.pop(-i)
        s.append(temp)
    return s


X = int(input())
s = list(input())

origin_s = s[:]
pattern = None

for i in range(1, X + 1):
    s = shuffle_s(s)
    if s == origin_s:
        pattern = i
        break

if pattern != None:
    X = X % pattern
s = origin_s

for i in range(X):
    s = shuffle_s(s)

res = ""

for i in s:
    res += i

print(res)
