with open(r'files/9.txt') as file:
    lines = [list(map(int, i.split())) for i in file]

for line in lines:
    if all(a < b for a, b in zip(line, line[1:])):
        if sum(1 for i in line if i % 2 == 0) ==  sum(1 for i in line if i % 2 != 0):
            print(line)

print(sum([10, 38, 59, 65, 70, 93]))