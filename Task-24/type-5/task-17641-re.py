from re import finditer
with open(r'/Users/admin/Desktop/N24/24_17641.txt') as file:
    data = file.readline()

num = r'(0|[1-9][0-9]*)'
prod = rf'({num}\*)*0(\*{num})*'
pattern = rf'({prod}\+)+{prod}'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))