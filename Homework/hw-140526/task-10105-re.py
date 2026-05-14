from re import finditer
with open(r'/Users/admin/Desktop/N24/24_10105.txt') as file:
    data = file.readline()

pattern = r'[^T]+(T[^T]*){100}[^T]*'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))