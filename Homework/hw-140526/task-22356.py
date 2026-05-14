from operator import index
from re import finditer

with open(r'/Users/admin/Desktop/N24/24_22356.txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]*[13579B]'
starts = [match.start() for match in finditer(pattern, data)]
matches = [match.group() for match in finditer(pattern, data)]
cl = matches + starts

max_m = pos = 0

for x in range(len(matches)):
    if int(matches[x], 12) > max_m:
        max_m = int(matches[x], 12)
        pos = x

print(cl[pos + len(matches)])