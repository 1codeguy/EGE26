from re import finditer

with open(r'../files/24_4627.txt') as file:
    data = file.readline()

patter = r'(NPO|PNO)+'

matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)) / 3)