# 2007년

month, date = map(int, input().split())

end_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
start_day = 1  # 1월 1일은 월요일
idx = start_day + ((sum(end_of_month[: month - 1]) + date - 1) % 7)
print(days[idx % 7 if idx >= 7 else idx])
