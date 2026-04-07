from re import finditer

with open(r'/Users/admin/Desktop/N24/24_18619.txt') as file:
    data = file.readline()

patter = r'[B]([1-6]+([-\*][1-6]+)+)'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))

