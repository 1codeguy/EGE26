with open(r'/Users/admin/Desktop/N24/24_13715.txt1') as file:
    data = file.readline()

data = data.split('AB')

ans = 0
for i in range(len(data) - 50):
    if i == 0 or i == len(data) - 51:
        ans = max(ans, len('AB'.join(data[i:i + 51])) + 1)
    else:
        ans = max(ans, len('AB'.join(data[i:i + 51])) + 2)

print(ans)