from string import ascii_uppercase

with open(r'/Users/admin/Desktop/N24/24-371.txt') as file:
    data = file.readline()

for i in ascii_uppercase:
    data = data.replace(i, '*')

data = data.replace('*.', '*. ')
data = data.split()

