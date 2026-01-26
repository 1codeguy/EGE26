from re import finditer

with open(r'/Users/admin/Desktop/N24/24_22359.txt') as file:
    data = file.readline()

patter = r'([1-9A-E][0-9A-E]*[05A])|([05A])'
matches = [match.group() for match in finditer(patter, data)]
max_str = (max(matches, key=lambda x: int(x, 15)))

print(data.index(max_str) + len(max_str) - 1)