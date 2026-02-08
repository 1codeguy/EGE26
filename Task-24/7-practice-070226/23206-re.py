from re import finditer

with open(r'/Users/admin/Desktop/N24/24_23206.txt') as file:
    data = file.readline()

patter = r'[02468]([^02468S]*S){35}[^02468S]*'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))