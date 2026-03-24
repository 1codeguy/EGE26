with open(r'/Users/admin/Desktop/N24/24_8510.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data) - 1):
    if data[i:i + 1] != 'NN' and \
            data[i:i + 1] != 'OO' and \
            data[i:i + 1] != 'PP':
        for j in range(i + 1, len(data) - 1):
            if data[j:j + 1] != 'NN' and \
                    data[j:j + 1] != 'OO' and \
                    data[j:j + 1] != 'PP':
                continue
            else:
                ans = max(ans, len(data[i:j + 1]))
                break

print(ans)
