with open(r'.\files\24 (1).txt') as file:
    data = file.readline()

data = data.split('Z')

ans = 10 ** 10
for i in range(len(data) - 268):
    line = 'Z'.join(data[i:i+269])
    ans = min(ans, len(line) + 2)

print(ans)