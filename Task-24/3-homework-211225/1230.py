from re import finditer

with open(r'/Users/admin/Desktop/N24/24_1230.txt') as file:
    data = file.readline()

# cnt = 0
# ans = 0
# for i in range(len(data)):
#     if data[i] not in 'WRQ':
#         cnt += 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 0
# ans = max(ans, cnt)
# print(ans)

#################

# for i in 'WRQ':
#     data = data.replace(i, ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

#################

pattern = r'[^WRQ]+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))