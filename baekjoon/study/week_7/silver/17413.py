# 단어 뒤집기 2


def empty_word():
    global word, res
    res += word[::-1]
    word = ""


string = input()
word = ""
tag = False
res = ""
for s in string:
    if s == "<":
        empty_word()
        tag = True
        res += s
        continue
    elif s == ">":
        tag = False
        res += s
        continue
    elif s == " ":
        empty_word()
        res += s
    else:
        if tag == True:
            res += s
        else:
            word += s
empty_word()

print(res)
