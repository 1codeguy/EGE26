from re import finditer

with open(r'/Users/admin/Desktop/N24/24_7624.txt') as file:
    data = file.readline()

patter = r'[^XYZ]*([XYZ][^XYZ]+)+[XYZ]?'

matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))