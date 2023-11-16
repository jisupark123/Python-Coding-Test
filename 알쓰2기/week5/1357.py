# 뒤집힌 덧셈


print(int(str(sum(map(lambda x: int(x[::-1]), input().split())))[::-1]))
