from re import finditer

with open(r'/Users/admin/Desktop/N24/24_17878.txt') as file:
    data = file.readline()

num = r'([^0\-\*][06-9]*|0)'
pattern = rf'({num}[-*])*{num}'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))