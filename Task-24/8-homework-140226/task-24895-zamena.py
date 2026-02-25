with open(r'/Users/admin/Desktop/N24/24_24895.txt') as file:
    data = file.readline()

data = data.replace('+', '*')
data = data.split('*')

ans = 0
for i in range(len(data) - 39):
    line = data[i:i+40]
    if '' not in line:
        ans = max(ans, len('*'.join(line)))

print(ans)