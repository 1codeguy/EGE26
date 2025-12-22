from re import*

with open(r'/Users/admin/Desktop/N24/24_4642.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in range(len(data) - 1):
#     if data[i] + data[i + 1] in 'A1 A2 B1 B2':
#         cnt = 1
#         for j in range(i + 2, len(data) - 1, 2):
#             if data[j] + data[j + 1] in 'A1 A2 B1 B2':
#                 cnt += 1
#             else:
#                 break
#         ans = max(ans, cnt)
#
# print(ans)

#################

# for i in ['A1', 'A2', 'B1', 'B2']:
#     data = data.replace(i, '*')
#
# data = data.replace('A', ' ')
# data = data.replace('B', ' ')
# data = data.replace('1', ' ')
# data = data.replace('2', ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

#################

pattern = r'([A-Z]\d)+'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 2)