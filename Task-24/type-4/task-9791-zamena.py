from string import ascii_uppercase
with open(r'../files/24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    ans = max(ans, len(line.lstrip('0')))

print(ans)

############################################

from string import ascii_uppercase
with open(r'../files/24_9791.txt') as file:
    data = file.readline()

for i in ascii_uppercase[6:]:
    data = data.replace(i, ' ')

data = data.replace('0', ' ')
while ' 0' in data:
    data = data.replace('0', ' ')

data = data.split()
print(len(max(data, key=len)))