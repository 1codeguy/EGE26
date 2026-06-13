from re import finditer

with open(r'files/24_27777.txt') as file:
    data = file.readline()

pattern = r'[1-9AB][0-9AB]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))