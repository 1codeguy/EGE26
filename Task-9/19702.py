from itertools import combinations

with open(r'.\files\19702.txt') as file:
    data = [list(map(int, i.split())) for i in file]

cnt = 0
for line in data:
    line = sorted(line, reverse=True)
    for a1, a2, a3, a4 in combinations(line, 4):
        if a1 - a2 == a2 - a3 == a3 - a4 != 0:
            cnt += 1
            break

print(cnt)