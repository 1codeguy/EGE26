from itertools import product

with open(r'../files/24_8510.txt') as file:
    data = file.readline()

for a in product('NOP', repeat=2):
    a = ''.join(a)
    while a in data:
        data = data.replace(a, f'{a[0]} {a[1]}')

data = data.split()

print(len(max(data, key=len)))
