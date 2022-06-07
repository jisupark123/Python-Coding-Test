# 요세푸스 문제

N, K = map(int, input().split())

circle = [x for x in range(1, N + 1)]
res = []

i = 0

for _ in range(N):
    cnt = 0
    while cnt != K:
        if i >= len(circle):
            i = 0
        elif circle[i] == False:
            i += 1
        else:
            cnt += 1
            if cnt == K:
                res.append(circle[i])
                circle[i] = False
            i += 1


print("<" + str(res)[1:-1] + ">")
