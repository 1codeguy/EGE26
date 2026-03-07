```
from re import *

with open(r'/Users/admin/Desktop/N24/24_22362.txt') as file:
    data = file.readline()

patter = r'[^C-Z]*'
res = [match.group() for match in finditer(patter, data)]

max_line = ''
for line in res:
    if int(line, 12) % 3 == 0:
        if len(line) > len(max_line):
            max_line = line

        elif len(line) == len(max_line) and \
                int(line, 12) < int(max_line, 12):
            max_line = line
```