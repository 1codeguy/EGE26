from re import finditer

with open(r'24.txt') as file:
    data = file.readline()

pattern = r'([7-9][0-9]*[\*\-])+[7-9][0-9]*'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
