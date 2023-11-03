import sys

input = sys.stdin.readline

N = int(input())

s = [
    "a",
    "b",
    "k",
    "d",
    "e",
    "g",
    "h",
    "i",
    "l",
    "m",
    "n",
    "ng",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "w",
    "y",
]

mapping = dict(zip(s, range(len(s))))
mapping_reverse = dict(zip(range(len(s)), s))
words = [input().strip() for _ in range(N)]

for i in range(len(words)):
    lst = []
    j = 0
    while j < len(words[i]):
        if words[i][j : j + 2] == "ng":
            lst.append("ng")
            j += 2
        else:
            lst.append(words[i][j])
            j += 1
    words[i] = lst


for i in range(len(words)):
    words[i] = list(map(lambda x: mapping[x], words[i]))

words.sort()

for w in words:
    res = ""
    for i in range(len(w)):
        res += mapping_reverse[w[i]]
    print(res)
