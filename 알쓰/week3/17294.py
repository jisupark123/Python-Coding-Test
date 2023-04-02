# 귀여운 수~ε٩(๑> ₃ <)۶з


def 공차수열인가():
    num = list(map(int, input().rstrip()))
    if len(num) == 1:
        return True
    d = num[1] - num[0]
    for i in range(2, len(num)):
        if d != num[i] - num[i - 1]:
            return False

    return True


print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!" if 공차수열인가() else "흥칫뿡!! <(￣ ﹌ ￣)>")
