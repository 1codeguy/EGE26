from re import finditer
with open(r'/Users/admin/Desktop/N24/24_12254.txt') as file:
    data = file.readline()

pattern = r'(SQ|Q)?(RSQ)+(RS|R)?'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))