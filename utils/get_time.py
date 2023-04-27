import timeit

start_time = timeit.default_timer()

num = 100000000
a = [False] * num
# a = [False for _ in range(num)]

print(f"{round(timeit.default_timer() - start_time,15)}초 걸렸습니다.")
print(f"{round(((timeit.default_timer() - start_time) * 1000),15)}ms 걸렸습니다.")
