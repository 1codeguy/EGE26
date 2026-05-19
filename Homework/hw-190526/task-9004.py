with open(r'/Users/admin/Desktop/N24/24-384.txt') as file:
    data = file.readline()

# data = '*** Z** Z* Z Z*** Z* Z'
pos_Z = [i for i in range(len(data)) if data[i] == 'Z']

ans = 10 ** 8
for x, y in zip(pos_Z, pos_Z[269:]):
    ans = min(ans, y - x + 1)
print(ans)