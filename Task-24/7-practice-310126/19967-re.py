from re import finditer

with open(r'/Users/admin/Desktop/N24/24_19967.txt') as file:
    data = file.readline()

num = '([1-9][0-9]*|0)'
patter = fr'(AFD){num}([\+\*]{num})+'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))