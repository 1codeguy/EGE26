with open(r'files/9.txt') as file:
    data = [list(map(int, i.split())) for i in file]

for pos, line in enumerate(data, start=1):
    amount = [line.count(i) for i in set(line)]
    if len(set(amount)) > 1:
        sum2pov = sum(i for i in line if line.count(i) > 1) ** 2
        sum2ne_pov = sum(i for i in line if line.count(i) == 1) ** 2
        if sum2pov > sum2ne_pov and sum(line) % 2 != 0 :
            print(pos)