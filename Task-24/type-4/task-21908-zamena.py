from string import ascii_uppercase
with open(r'../files/24_21908 (1).txt') as file:
    data = file.readline()

for i in ascii_uppercase[4:]:
    data = data.replace(i, ' ')

data = data.split()

ans = 0
for line in data:
    line = line.lstrip('0').rstrip('13579BD')
    ans = max(ans, len(line))

print(ans)