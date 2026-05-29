from re import finditer

with open(r'/Users/admin/Desktop/N24/24_5171.txt') as file:
    data = file.readline()

pattern = r'(CA)+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))