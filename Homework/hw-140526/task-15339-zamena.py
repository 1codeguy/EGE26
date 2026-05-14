import re
from os import fwalk

with open(r'/Users/admin/Desktop/N24/24_15339.txt') as file:
    data = file.readline()

for i in 'ABC':
    data = data.replace(i, '#')
for i in '6789':
    data = data.replace(i, '%')

data = re.split(r'%%|##', data)

ans = 0
string = []
max_pos = 0
for pos, line in enumerate(data):
    if len(line) == 1 and line[0] == string[-1] and pos - 1 == max_pos:
        string += line
    elif len(line) > ans:
        ans = max(ans, len(line))
        string = []
        string += line

print(ans)
print(string)