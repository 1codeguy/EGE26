from re import finditer

with open(r'/Users/admin/Desktop/N24/24_25361.txt') as file:
    data = file.readline()

patter = r'[02468]([^02468F]*F){76}[^02468F]*'
matches = [match.group() for match in finditer(patter, data)]
print(len(max(matches, key=len)))