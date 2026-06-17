with open(r'files/28930.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

cnt = 0
for line in lines:
    flag = True
    for a, b in zip(line, line[1:]):
        if a < b:
            continue
        else:
            flag = 0
            break
    if flag:
        if max(line) + min(line) <= sum(line) - max(line) - min(line):
            cnt += 1

print(cnt)