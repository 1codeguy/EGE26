with open(r'/Users/admin/Desktop/N24/24_12254.txt') as file:
    data = file.readline()

len_data = len(data)
ans = i = 0

while i < len_data:
    if data[i:i + 3] == 'RSQ':
        start = i
        while i + 3 <= len_data and data[i:i + 3] == 'RSQ':
            i += 3
        end = i
        left = 0
        if start >= 2 and data[start - 2:start] == 'SQ':
            left = 2
        elif start >= 1 and data[start - 1] == 'Q':
            left = 1
        right = 0
        if end + 1 < len_data and data[end:end + 2] == 'RS':
            right = 2
        elif end < len_data and data[end] == 'R':
            right = 1
        len_line = end - start + left + right
        ans = max(ans, len_line)
    else:
        i += 1

print(ans)
# using ai