from re import*

with open(r'/Users/admin/Desktop/N24/24_3228.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in range(len(data) - 1):
#     if data[i] + data[i + 1] in 'AC AB':
#         cnt = 1
#         for j in range(i + 2, len(data) - 1, 2):
#             if data[j] + data[j + 1] in 'AC AB':
#                 cnt += 1
#             else:
#                 break
#         ans = max(ans, cnt)
#
# print(ans)

#######################

# for i in ['AB', 'AC']:
#     data = data.replace(i, '*')
#
# for i in 'ABC':
#     data = data.replace(i, ' ')
#
# data = data.split()
#
# print(len(max(data, key=len)))

#######################

pattern = r'(AB|AC)+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)) // 2)
