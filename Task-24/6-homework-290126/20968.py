from re import finditer

with open(r'/Users/admin/Desktop/N24/24_20968.txt') as file:
    data = file.readline()

patter = r'[1-9][0-9]*[02468]([+*][1-9][0-9]*[02468])*'
matches = [match.group() for match in finditer(patter, data)]

print(len(max(matches, key=len)),max(matches, key=len))