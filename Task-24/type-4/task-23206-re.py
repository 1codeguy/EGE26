from re import finditer

with open(r'../files/24_23206.txt') as file:
    data = file.readline()

pattern = r'[02468]([^02468S]*S){35}[^02468S]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))