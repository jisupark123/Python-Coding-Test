# 찾기


def kmp(T, P):
    p = [0] * len(P)  # i번째에서 틀린다면 p[i-1]에서부터 다시 시작

    j = 0
    for i in range(1, len(P)):
        while j != 0 and P[i] != P[j]:
            j = p[j - 1]

        if P[i] == P[j]:
            j += 1
            p[i] = j

    ans = []

    j = 0
    for i in range(len(T)):

        # 문자열 매칭 실패하면 p[j-1]부터 다시 시작
        while j != 0 and T[i] != P[j]:
            j = p[j - 1]
        if T[i] == P[j]:
            if j == len(P) - 1:
                ans.append(i - len(P) + 2)
                j = p[j]  # 문자열 매칭에 성공하면 특정 포인트부터 다시 시작
            else:
                j += 1

    print(len(ans))
    if len(ans):
        print(*ans)


T = input()
P = input()

kmp(T, P)

# ABCDABABCDABD
# ABCDABD
