from re import finditer

with open(r'/Users/admin/Desktop/N24/24_22446.txt') as file:
    data = file.readline()

data.split('LND')
ans = 0

for i in range(len(data) - 10_000):
    line = 'LND'.join(data[i:i + 10_001])
    if line[0] == line[-1]:
        ans = max(ans, len(line))

print(ans)

# patter = r'(LND)'
# matches = [match.group() for match in finditer(patter, data)]
# print(len(max(matches, key=len)))