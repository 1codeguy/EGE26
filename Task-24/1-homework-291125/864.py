from re import *

with open(r'/Users/admin/Desktop/24_864.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in range(len(data)):
#     if data[i] not in 'AE':
#         cnt += 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 0
# ans = max(ans, cnt)
#
# print(ans)

# while 'A' in data or 'E' in data:
#     data = data.replace('A', ' ')
#     data = data.replace('E', ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

pattern = r'[^AE]+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))