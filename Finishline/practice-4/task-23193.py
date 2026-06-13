with open(r'files/9.txt') as file:
    lines = [list(map(int, i.split())) for i in file]


for pos, line in enumerate(lines, 1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 3]:
        pov = sum(i for i in line if line.count(i) > 1)
        ne_pov = [i for i in line if line.count(i) == 1]
        sr = sum(ne_pov) / len(ne_pov)
        if pov > sr:
            print(pos)