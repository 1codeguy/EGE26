from re import finditer

with open(r'/Users/admin/Desktop/N24/24_6757.txt') as file:
    data = file.readline()

patter = r'(CFE|FCE)+'

matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)) / 3)