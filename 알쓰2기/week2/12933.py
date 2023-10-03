s = list(input().strip())
quack = "quack" * 500

res = 0
for i in range(len(s)):
    if s[i] == 0:
        continue
    q = 0
    idx_to_remove = []
    for j in range(i, len(s)):
        if s[j] == quack[q]:
            idx_to_remove.append(j)
            q += 1

    for k in range(len(idx_to_remove) // 5 * 5):
        s[idx_to_remove[k]] = 0

    if len(idx_to_remove) // 5 * 5 >= 5:
        res += 1

if len(list(filter(lambda x: x != 0, s))) == 0:
    print(res)
else:
    print(-1)
