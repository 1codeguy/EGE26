from re import finditer
with open(r'/Users/admin/Desktop/N24/24-295.txt') as file:
    data = file.readline()

pattern = r'DE'

index = [match.start() for match in finditer(pattern, data)]

max_len_line = 0
for i in range(1, len(index) - 239 - 1):
    previous_start = index[i - 1]
    next_end = index[i + 240]
    full_len_line = next_end - previous_start
    max_len_line = max(max_len_line, full_len_line)

print(max_len_line)

