# 팰린드롬인지 확인하기

# s[::-1] -> 문자열 뒤집는 문법

s = input()
print(1 if s == s[::-1] else 0)
