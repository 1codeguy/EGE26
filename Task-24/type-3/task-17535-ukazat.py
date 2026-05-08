with open(r'../files/24_17535.txt') as file:
    data = file.readline()

ans = cnt = r = l = 0

len_data = len(data)
while r < len_data:
    if cnt <= 160:
        if data[r:r + 2] == 'CD': cnt += 1
        r += 1
    else:
        if data[l:l + 2] == 'CD': cnt -= 1
        l += 1
    ans = max(ans, r - l)

print(ans)