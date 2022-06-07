# 물병

N, K = map(int, input().split())

count = 0
while bin(N).count("1") > K:
    N += 1
    count += 1
print(count)
