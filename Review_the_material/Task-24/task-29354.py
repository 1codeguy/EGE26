with open(r'files/24_29354.txt') as file:
    data = file.readline()

data = data.split('BC')

#         [                         ]
#data = 'BC*****BC****BC*****BC*****BC'

ans = 0
for i in range(len(data) - 190):
    line = 'BC'.join(data[i:i + 191])
    ans = max(ans, len(line) + 2)

print(ans)