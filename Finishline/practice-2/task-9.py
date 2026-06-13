with open(r'files/9.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

max_num = 0
for pos, line in enumerate(lines, 1):
    if len(set(line)) == len(line):
        if 2 * (max(line) + min(line)) == 3 * (sum(line) - (max(line) + min(line))):
            print(pos)