import timeit


start_time = timeit.default_timer()


print(f"{round(timeit.default_timer() - start_time,15)}초 걸렸습니다.")
print(f"{round(((timeit.default_timer() - start_time) * 1000),15)}ms 걸렸습니다.")
