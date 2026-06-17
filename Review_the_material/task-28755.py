with open(r'files/28755.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

cnt = 0
for line in lines:
    if max(line) < sum(line) - max(line):
        if min(line) + max(line) != sum(line) - min(line) - max(line):
            cnt += 1

print(cnt)