from string import ascii_uppercase

with open(r'/Users/admin/Desktop/N24/24_14510.txt') as file:
    data = file.readline()

for i in ascii_uppercase:
    if i in 'AEIOYU':
        data = data.replace(i, '*')
    else:
        data = data.replace(i, '-')

data = data.split('--*')

ans = 10**20
for i in range(len(data) - 498 - 1):
    ans = min(ans, len('--*'.join(data[i:i+499])) + 6)
print(ans)