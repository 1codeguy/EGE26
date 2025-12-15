from re import *

with open(r'/Users/admin/Desktop/24_865.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in range(len(data)):
#     if data[i] != 'C' and data[i] != 'F':
#         cnt += 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 0
# ans = max(ans, cnt)
#
# print(ans)

######################

# while 'C' in data or 'F' in data:
#     data = data.replace('C', ' ')
#     data = data.replace('F', ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

######################

pattern = r'[^CF]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))