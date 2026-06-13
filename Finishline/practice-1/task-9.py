with open(r'files/9.txt') as file:
    lines = [list(map(int, i.split())) for i in file]


cnt = 0
for line in lines:
    U1 = sum(line) - max(line) > max(line)
    U2 = len(line) - len(set(line)) == 1
    if U1 and U2:
        cnt += 1

print(cnt)