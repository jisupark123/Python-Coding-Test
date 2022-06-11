# 평균

N = int(input())
grades = list(map(int, input().split()))
max_grade = max(grades)
grades = list(map(lambda x: x / max_grade * 100, grades))

print(sum(grades) / len(grades))
