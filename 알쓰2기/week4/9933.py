import sys

input = lambda: sys.stdin.readline().strip()

N = int(input())

words = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if words[i] == words[j][::-1]:
            print(len(words[i]), words[i][len(words[i]) // 2])
            exit(0)
