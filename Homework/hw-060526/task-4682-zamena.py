with open(r'/Users/admin/Desktop/N24/24_4682.txt') as file:
    data = file.readline()

for i in 'AE':
    data = data.replace(i, '*')

for i in 'BCD':
    data = data.replace(i, '#')

data = data.replace('*#', '!')

for i in data:
    if i != '!':
        data = data.replace(i, ' ')

print(data)

print(len(max(data, key=len)))