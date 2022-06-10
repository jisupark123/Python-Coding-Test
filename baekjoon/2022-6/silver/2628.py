# 종이자르기

width, height = map(int, input().split())
N = int(input())
width_cuts, height_cuts = [0], [0]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        width_cuts.append(b)
    else:
        height_cuts.append(b)
width_cuts.sort()
height_cuts.sort()
width_cuts.append(height)
height_cuts.append(width)

max_width = 0

for w in range(1, len(width_cuts)):
    for h in range(1, len(height_cuts)):
        new_area = (width_cuts[w] - width_cuts[w - 1]) * (
            height_cuts[h] - height_cuts[h - 1]
        )
        if new_area > max_width:
            max_width = new_area

print(max_width)
