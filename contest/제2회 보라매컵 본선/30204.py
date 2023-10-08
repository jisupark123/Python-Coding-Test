# 병영외 급식
N, X = map(int, input().split())
print(1 if sum(list(map(int, input().split()))) % X == 0 else 0)
