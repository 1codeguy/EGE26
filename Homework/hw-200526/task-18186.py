with open(r'/Users/admin/Desktop/N24/24_18186.txt') as file:
    data = file.readline()

for i in 'AE':
    data = data.replace(i, '#')
for i in 'BCDFGH':
    data = data.replace(i, '@')

data = data.replace('@@#', '*** ***')
print(data.find('@#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@***'))
print(data[2363480:2363486+62])

data = data.split()

print(len(max(data, key=len)))
print(max(data, key=len))