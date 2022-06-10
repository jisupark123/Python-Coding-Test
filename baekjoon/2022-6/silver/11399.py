# ATM
N = input()
times = list(map(int, input().split()))
times.sort()
for i in range(1, len(times)):
    times[i] = times[i - 1] + times[i]

print(sum(times))
