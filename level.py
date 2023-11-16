import random
from collections import defaultdict

members = ["박지수", "정지수", "상민", "은빈", "범수", "영은"]
problems = {"Gold": 3, "Silver": 4, "Bronze": 5}

while True:
    problem_list = []
    for key in problems.keys():
        for _ in range(problems[key]):
            problem_list.append(key)

    res = defaultdict(list)

    for member in members:
        for _ in range(2):
            i = random.randint(0, len(problem_list) - 1)
            res[member].append(problem_list[i])
            del problem_list[i]

    flag = True
    for key in res:
        if res[key].count("Gold") == 2 or res[key].count("Bronze") == 2:
            flag = False
            break

    if flag:
        break

for key in res:
    print(key, "-", ", ".join(res[key]))
