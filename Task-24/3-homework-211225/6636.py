from re import finditer

with open(r'/Users/admin/Desktop/N24/24_6636.txt') as file:
    data = file.readline()

# ch = '24'
# nch = '135'
# cnt = 0
# ans = 0
# for i in range(len(data) - 1):
#     if data[i] in ch and data[i + 1] in nch:
#         cnt = 1
#         for j in range(i + 2, len(data) - 1, 2):
#             if data[j] in ch and data[j + 1] in nch:
#                 cnt += 1
#             else:
#                 ans = max(ans, cnt)
#                 break
# ans = max(ans, cnt)
# print(ans)

######################

# for i in '24':
#     data = data.replace(i, '*')
#
# for i in '135':
#     data = data.replace(i, '-')
#
# data = data.replace('*-', '+')
#
# for i in '*-':
#     data = data.replace(i, ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

######################

ch = '[24]'
nch = '[135]'
pattern = fr'({ch}{nch})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)
