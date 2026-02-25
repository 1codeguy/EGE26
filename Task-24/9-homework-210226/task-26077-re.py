from re import finditer

with open(r'/Users/admin/Desktop/N24/24_26077.txt') as file:
    data = file.readline()

patter = r'G([02468A-FH-Z]*[13579]){45}[02468A-FH-Z]*'
matches = [match.group() for match in finditer(patter, data)]

print(len(max(matches, key=len)))