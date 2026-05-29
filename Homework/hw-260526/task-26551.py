from re import finditer

with open(r'/Users/admin/Desktop/N24/24_26551.txt') as file:
    data = file.readline()

pattern = r'[^0][0-9A-D]*[02468AC]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))