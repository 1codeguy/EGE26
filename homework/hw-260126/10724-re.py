from re import finditer

with open(r'/Users/admin/Desktop/N24/24_10724.txt') as file:
    data = file.readline()

patter = r'([1-9A-F][0-9A-F]*)'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))