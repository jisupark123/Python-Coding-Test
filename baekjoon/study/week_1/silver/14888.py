# 연산자 끼워넣기

# 순열을 이용한 방법

# from itertools import permutations
# import sys

# # ex) [1,2,3,4], ['+','-','/'] 형식의 매개변수가 주어지면 계산값을 반환하는 함수
# def calculator(nums, operators):
#     res = nums[0]
#     for i in range(len(operators)):
#         if operators[i] == "+":
#             res += nums[i + 1]
#         elif operators[i] == "-":
#             res -= nums[i + 1]
#         elif operators[i] == "*":
#             res *= nums[i + 1]
#         else:
#             if res >= 0:
#                 res //= nums[i + 1]
#             else:
#                 res = -res // nums[i + 1]
#                 res = -res
#     return res


# input = sys.stdin.readline

# N = int(input())
# nums = list(map(int, input().split()))

# # 주어진 숫자를 연산자로 변환
# operators_input = list(map(int, input().split()))
# operators_def = ["+", "-", "*", "/"]
# operators = []
# for i in range(4):
#     for _ in range(operators_input[i]):
#         operators.append(operators_def[i])

# max_num = -1e9
# min_num = 1e9

# # 순열을 하나하나 순회하면서 max_num, min_num과 비교
# for combi in permutations(operators):
#     max_num = max([calculator(nums, combi), max_num])
#     min_num = min([calculator(nums, combi), min_num])
# print(max_num)
# print(min_num)


# 백트래킹 (DFS)를 이용한 방법

import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_num = -1e9
min_num = 1e9

# +,-,*,/ 모든 경우의수에서 동시다발적으로 재귀함수 호출
# 단계를 지날 때마다 total값 누적
# 만약 숫자들을 모두 순회하면 최댓값,최솟값 비교
def dfs(depth, total, plus, minus, multiply, divide):
    global max_num, min_num
    if depth == N:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], operators[0], operators[1], operators[2], operators[3])
print(max_num)
print(min_num)
