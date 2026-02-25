with open(r'/Users/admin/Desktop/N24/24_26077.txt') as file:
    data = file.readline()

for i in '13579':
    data = data.replace(i, '*')

data = data.split('G')

ans = 0
for line in data:
    if line.count('*') == 45:
        ans = max(ans, len(line) + 1)
    elif line.count('*') > 45:
        while line.count('*') > 45:
            line = line[:-1]
        ans = max(ans, len(line) + 1)

print(ans)