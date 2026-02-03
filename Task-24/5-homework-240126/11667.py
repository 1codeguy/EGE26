with open(r'/Users/admin/Desktop/N24/24_11667.txt') as file:
    data = file.readline()

data = data.split('INFINITY')

ans = 0
for i in range(len(data) - 1000):
    if i == 0 or i == len(data) - 1001:
        ans = max(ans, len('INFINITY'.join(data[i:i + 1001])) + 7)
    else:
        ans = max(ans, len('INFINITY'.join(data[i:i + 1001])) + 14)

print(ans)