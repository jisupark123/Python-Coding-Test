import sys

input = sys.stdin.readline


def rounded(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)


n = int(input())


scores = [int(input()) for _ in range(n)]
scores.sort()

if len(scores) == 0:
    print(0)
    exit(0)

cut = rounded(len(scores) * 0.15)
scores = scores[cut : n - cut]
print(rounded(sum(scores) / len(scores)))
