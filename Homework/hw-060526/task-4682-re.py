from re import finditer

with open(r'/Users/admin/Desktop/N24/24_4682.txt') as file:
    data = file.readline()

patter = r'([AE][^AE])+'

matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)) / 2)