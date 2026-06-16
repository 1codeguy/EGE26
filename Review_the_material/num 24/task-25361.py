from re import finditer

with open(r'files/24_25361 (1).txt') as file:
    data = file.readline()

pattern = r'[02468]([^02468F]*F){76}[^02468F]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))