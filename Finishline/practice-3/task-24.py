from re import finditer

with open(r'files/24_28006.txt') as file:
    data = file.readline()

num = r'\([1-9][0-9]*[02468][+|-][1-9][0-9]*[13579]\)'
pattern = fr'({num})+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))