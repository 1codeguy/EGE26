with open(r'files/9778.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 1, 2]:
        mid = sum(i for i in line if line.count(i) == 1)
        pov = sum(i for i in line if line.count(i) > 1) / 2
        if pov >= mid / 4:
            print(pos)
            break