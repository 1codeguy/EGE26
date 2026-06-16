with open(r'files/9.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

ans = 0
for pos, line in enumerate(lines, 1):
    if len(set(line)) == len(line):
        cube = (max(line) - min(line)) ** 3
        square = (sum(line) - max(line) - min(line)) ** 2
        if cube >= square:
            ans += pos

print(ans)