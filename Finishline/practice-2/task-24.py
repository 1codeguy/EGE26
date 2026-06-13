from string import digits

with open(r'files/24_23381.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, '* *')

data = data.split()

max_len = 0
for line in data:
    if digits not in line:
        max_len = max(max_len, len(line))
    else:
        while digits in line:
            line = line[1:]
            if digits in line:
                line = line[:-1]
        max_len = max(max_len, len(line))

print(max_len)
