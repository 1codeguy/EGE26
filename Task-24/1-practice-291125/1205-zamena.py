with open(r'/Users/admin/Desktop/24_1205.txt') as file:
    data = file.readline()

for i in 'GWP':
    data = data.replace(i, ' ')
data = data.split()
print(len(max(data, key=len)))