with open(r'/Users/admin/Desktop/N24/24_23206.txt') as file:
    data = file.readline()

for i in '02468':
    data = data.replace(i, ' 0')

data = data.split()

ans = 0
for line in data:
    if line.count('S') == 35:
        ans = max(ans, len(line))
    elif line.count('S') > 35:
        pos_S = [i for i in range(len(line)) if line[i] == 'S']
        ans = max(ans, len(line[:pos_S[35]]))

print(ans)
