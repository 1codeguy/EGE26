with open(r'files/29962.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(lines, 1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 3]:
        pov = sum(i for i in line if line.count(i) > 1)
        ne_pov = sum(i for i in line if line.count(i) == 1) / 4
        if ne_pov > pov:
            print(pos)