from re import finditer

with open(r'/Users/admin/Desktop/N24/24_7600.txt') as file:
    data = file.readline()

patter = r'[^QRS]*([QRS][^QRS]+)+[QRS]?'

matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))