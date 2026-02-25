with open(r'/Users/admin/Desktop/N24/24_26078.txt') as file:
    data = file.readline()

data.split('W')

ans = 0
for i in range(len(data) - 90):
    line = 'W'.join(data[i:i+91])
    if line.count('2025') >= 110:
        ans = max(ans, len(line))

print(ans)