from re import finditer

with open(r'/Users/admin/Desktop/N24/24_4710.txt') as file:
    data = file.readline()

# vow = 'AO'
# con = 'CDF'
# cnt = 0
# ans = 0
# for i in range(len(data) - 1):
#     if data[i] in con and data[i + 1] in vow:
#         cnt = 1
#         for j in range(i + 2, len(data) - 1, 2):
#             if data[j] in con and data[j + 1] in vow:
#                 cnt += 1
#             else:
#                 ans = max(ans, cnt)
#                 break
# ans = max(ans, cnt)
# print(ans)

#######################

# for i in 'AO':
#     data = data.replace(i, '-')
#
# for i in 'CDF':
#     data = data.replace(i, '*')
#
# data = data.replace('*-', '+')
#
# for i in '*-':
#     data = data.replace(i, ' ')
#
# data = data.split()
#
# print(len(max(data, key=len)))

#######################

vow = '[AO]'
con = '[CDF]'
pattern = fr'({con}{vow})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)