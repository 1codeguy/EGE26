with open(r'/Users/admin/Desktop/N24/24_23381.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    if data[i] in '02468':
        for j in range(i + 2, len(data)):
            if data[j] in '13579':
                break
            if data[j] in '02468':
                if all(data[i + 1:j].count(let) > 1 for let in set(data[i + 1:j])):
                    ans = max(ans, j - i + 1)
                break

print(ans)