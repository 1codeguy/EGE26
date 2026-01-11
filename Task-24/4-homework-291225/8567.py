with open(r'/Users/admin/Desktop/N24/24_8567.txt') as file:
    data = file.readline()

for i in 'ABCD':
    data = data.replace(i, '*')

data = data.split('***')
print(len(max(data, key=len)) + 4)
