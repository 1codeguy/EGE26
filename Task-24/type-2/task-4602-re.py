from re import finditer

with open(r'../files/24_4602.txt') as file:
    data = file.readline()

patter = r'([BCD][AO])+'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)) / 2)