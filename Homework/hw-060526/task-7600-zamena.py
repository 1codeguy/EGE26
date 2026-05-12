from itertools import product
with open(r'/Users/admin/Desktop/N24/24_7600.txt') as file:
    data = file.readline()

for line in product('QRS', repeat=2):
    line = ''.join(line)
    data = data.replace(line, '# #')

data = data.split()

print(len(max(data, key=len)))
