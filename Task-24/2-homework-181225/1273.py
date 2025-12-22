from multiprocessing.forkserver import connect_to_new_process
from re import*

with open(r'/Users/admin/Desktop/N24/24_1273 (1).txt') as file:
    data = file.readline()

# ans = 0
# cnt = 2
# for i in range(len(data) - 2):
#     if data[i:i + 3] != 'XYZ':
#         cnt += 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 2
# ans = max(ans, cnt)
#
# print(ans)

######################

# data = data.replace('XYZ', 'XY YZ')
#
# data = data.split()
# print(len(max(data, key=len)))


pattern = r'(^|(?<=(XYZ))).+?($|(?=(XYZ)))'
ans = 0
for match in finditer(pattern, data):
    cnt_XYZ = match.groups().count('XYZ')
    ans = max(ans, len(match.group()) + 4 if cnt_XYZ == 2 else 2)
print(ans)
