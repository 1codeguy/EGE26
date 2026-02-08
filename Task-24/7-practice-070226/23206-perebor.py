with open(r'/Users/admin/Desktop/N24/24_23206.txt') as file:
    data = file.readline()

ans = 0
for i in range(len(data)):
    if data[i] in '02468':
        cnt_S = 0
        for j in range(i + 1, len(data)):
            if data[j] == 'S':
                cnt_S += 1
            if data[j] in '02468':
                if cnt_S == 35:
                    ans = max(ans, j - i)
                break
            if cnt_S == 36:
                ans = max(ans, j - i)
                break

print(ans)