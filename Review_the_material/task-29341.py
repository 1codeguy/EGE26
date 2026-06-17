from itertools import combinations

with open(r'files/29341.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

cnt = 0
for line in lines:
    if max(line) < sum(line) - max(line):
        sums = []
        if max(line) + min(line) != sum(line) - max(line) - min(line):
            cnt += 1

print(cnt)