# 알파벳 찾기


S = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"

idx_dict = {}

for i in range(len(S)):
    if S[i] not in idx_dict:
        idx_dict[S[i]] = i

for alphabet in alphabets:
    try:
        print(idx_dict[alphabet], end=" ")
    except:
        print(-1, end=" ")
