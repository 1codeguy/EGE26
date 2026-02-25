
with open(r'/Users/admin/Desktop/N24/24_25361.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')


data = data.split()

ans = 0
for line in data:
    if line.count('F') == 76:
        ans = max(ans, len(line))
    elif line.count('F') > 76:
        pos_F = [i for i in range(len(line)) if line[i] == 'F']
        ans = max(ans, len(line[:pos_F[76]]))
        while line.count('F') > 76:
            line = line[:-1]
        ans = max(ans, len(line))
print(ans)
