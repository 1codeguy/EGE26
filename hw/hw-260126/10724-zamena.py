from string import ascii_uppercase, digits

with open(r'/Users/admin/Desktop/N24/24_10724.txt') as file:
    data = file.readline()

alph = ascii_uppercase[:6]

for i in data:
    if i not in f'{digits}{alph}':
        data = data.replace(i, '')

data = data.split('')

print(len(max(data, key=len)))
