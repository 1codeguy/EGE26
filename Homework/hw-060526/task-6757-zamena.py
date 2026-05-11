with open(r'/Users/admin/Desktop/N24/24_6757.txt') as file:
    data = file.readline()

data = data.replace('CFE', '#')
data = data.replace('FCE', '#')

for i in data:
    if i != '#':
        data = data.replace(i, ' ')
        
data = data.split()

print(len(max(data, key=len)))