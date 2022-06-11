# 단어 공부

string = input().upper()

alphabet = ""
cnt = 0

for s in set(string):
    s_cnt = string.count(s)
    if s_cnt > cnt:
        alphabet = s
        cnt = s_cnt
    elif s_cnt == cnt:
        alphabet = "?"

print(alphabet)
