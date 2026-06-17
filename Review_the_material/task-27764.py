with open(r'files/27764.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

cnt = 0
for line in lines:
    if len(set(line)) == len(line):
        if (max(line) + min(line)) * 2 == sum(line) - max(line) - min(line):
            cnt += 1

print(cnt)