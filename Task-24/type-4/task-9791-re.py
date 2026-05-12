from re import finditer
from string import printable
print(printable[:16])
with open(r'../files/24_9791.txt') as file:
    data = file.readline()

pattern = r'[1-9A-F][0-9A-F]*|0'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))