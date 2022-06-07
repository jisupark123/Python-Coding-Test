# 랜덤 비밀번호 생성기

import random

alphabets = list(range(97, 123))  # 아스키코드 a ~ z
special_chrs = ["!", "@", "#", "%", "&"]
numbers = list(range(0, 10))

res = []

for _ in range(5):
    res.append(chr(random.choice(alphabets)))
for _ in range(4):
    res.append(str(random.choice(numbers)))
for _ in range(3):
    res.append(random.choice(special_chrs))


random.shuffle(res)

print("".join(res))
