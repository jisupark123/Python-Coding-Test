# OX퀴즈

T = int(input())

for _ in range(T):
    ox = input()
    score = 0
    combo = 0
    for s in ox:
        if s == "O":
            score += combo + 1
            combo += 1
        else:
            combo = 0
    print(score)
