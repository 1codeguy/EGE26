with open(r'../files/24_4602.txt') as file:
    data = file.readline()

for i in 'AO':
    data = data.replace(i, '#')
for i in 'BCD':
    data = data.replace(i, '!')

for i in ['!#']:
    data = data.replace(i, '*')

for i in '#!':
    data = data.replace(i, ' ')

data = data.split()

print(len(max(data, key=len)))
