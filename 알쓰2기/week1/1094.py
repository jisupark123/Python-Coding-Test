x = int(input())

sticks = [64]
while sum(sticks) > x:
    sticks.sort(reverse=True)
    # 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
    sticks[-1] = sticks[-1] // 2
    sticks.append(sticks[-1])
    # 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
    if sum(sticks[:-1]) >= x:
        sticks = sticks[:-1]

print(len(sticks))
