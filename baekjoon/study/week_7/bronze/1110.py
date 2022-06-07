# 더하기 사이클

N = input()
if int(N) < 10:
    N = "0" + N  # 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만든다
start = N
res = 0

while N != start or res == 0:  # N이 돌고 돌아 처음 숫자랑 같아지면 반복문을 종료한다.
    sum_num = sum(map(int, list(str(N))))  # 76 -> 7+6 -> 13
    N = N[-1] + str(sum_num)[-1]  # 76의 6과 13의 3을 합치면 63
    res += 1

print(res)
