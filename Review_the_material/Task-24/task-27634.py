with open(r'files/24_27634.txt') as file:
    data = file.readline()

data = data.split('Z')

# data = '***Z****Z******Z***'
ans = 10 ** 8
for i in range(len(data) - 268):
    line = 'Z'.join(data[i:i + 269])
    ans = min(ans, len(line) + 2)

print(ans)