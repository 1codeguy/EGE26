with open(r'.\files\24 (1).txt') as file:
    data = file.readline()

data = data.split('Z')

ans = 10 ** 10
for i in range(len(data) - 270):
    line = 'Z'.join(data[i:i+271])
    ans = min(ans, len(line))

print(ans)