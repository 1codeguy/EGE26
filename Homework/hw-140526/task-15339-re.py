from re import finditer
with open(r'/Users/admin/Desktop/N24/24_15339.txt') as file:
    data = file.readline()

pattern = r'([ABC][6-9])+[ABC]?|([6-9][ABC])+[6-9]?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
print(max(matches, key=len))