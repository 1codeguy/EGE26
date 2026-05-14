with open(r'/Users/admin/Desktop/N24/24_10105.txt') as file:
    data = file.readline()

s = data
data = data.split('T')

ans = 0
for i in range(len(data) - 99):
    line = 'T'.join(data[i:i + 100])
    len_line = len(line)

print(ans)