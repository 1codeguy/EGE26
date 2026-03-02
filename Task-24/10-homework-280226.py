with open(r'/Users/admin/Desktop/N24/24_14512.txt') as file:
    data = file.readline()

data = data.replace('1', '1 1')
data = data.replace('8', '8 8')
data = data.split()

ans = 0
for line in data:
    if int(line[0], 36) + int(line[-1], 36) == 9 and line.count('B') == line.count('C'):
            ans = max(ans, len(line))

print(ans)