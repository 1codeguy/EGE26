from re import finditer

with open(r'/Users/admin/Desktop/N24/24_1428.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in range(len(data) - 1):
#     if data[i] + data[i + 1] not in 'XY XZ':
#         cnt = 1
#         for j in range(i + 2, len(data) - 2):
#             if data[j] + data[j + 1] not in 'XY XZ':
#                 cnt += 1
#             else:
#                 ans = max(ans, cnt)
#                 break
# ans = max(ans, cnt)
# print(ans)

#####################

# data = data.replace('XY', 'X Y')
# data = data.replace('XZ', 'X Z')
#
# data = data.split()
# print(len(max(data, key=len)))

#####################

pattern = r'(^|(?<=(XY|XZ))).+?($|(?=(XY|XZ)))'
ans = 0
for match in finditer(pattern, data):
    cnt_XY_XZ = match.groups().count('XY') + match.groups().count('XZ')
    ans = max(ans, len(match.group()) + 2 if cnt_XY_XZ == 2 else 1)
print(ans)