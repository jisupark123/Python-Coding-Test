import random
from collections import defaultdict

members = ["지수", "상민", "희윤", "혜연", "은빈", "민희", "채연", "범수"]
problems = {"Gold": 2, "Silver": 10, "Bronze": 4}

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
