# 문자열 폭발
# s = input().strip()
# pop_s = input().strip()

s = "12ab112ab2ab" * 1000000
pop_s = "12ab"


# 처음 제출 -> 파이썬 내장함수 replace 이용 but 시간초과
# 100,000,000 -> 4.72초
# while True:
#     new_x = s.replace(pop_s, "")
#     if len(new_x) == 0:
#         print("FRULA")
#         break
#     if len(new_x) == len(s):
#         print(new_x)
#         break
#     s = new_x


# i = 0
# while True:
#     if len(s) == 0:
#         print("FRULA")
#         break
#     if i + len(pop_s) > len(s):
#         print(s)
#         break
#     if s[i : i + len(pop_s)] == pop_s:
#         s = s[:i] + s[i + len(pop_s) :]
#         i -= len(pop_s)
#     else:
#         i += 1

s = input().strip()
pop_s = input().strip()
pop_len = len(pop_s)

# 두번째 답 -> 스택을 이용 -> 문자열 합치기 비용 X and 한 번만 순회할 수 있음
stack = []

for u in s:
    stack.append(u)
    if len(stack) >= pop_len and "".join(stack[-pop_len:]) == pop_s:
        for _ in range(pop_len):
            stack.pop()

print("FRULA" if len(stack) == 0 else "".join(stack))
