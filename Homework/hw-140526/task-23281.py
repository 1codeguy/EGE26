from string import ascii_uppercase

with open(r'/Users/admin/Desktop/N24/24_23381.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    if all(i not in '13579' for i in line):
        flag = True
        for i in line:
            if i not in ascii_uppercase:
                continue
            elif i in ascii_uppercase and i != line[0]:
                flag = False
        if flag:
            ans = max(ans, len(line) + 2)

print(ans)