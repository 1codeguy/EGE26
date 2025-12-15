from re import*

with open(r'/Users/admin/Desktop/24_1146.txt') as file:
    data = file.readline()

# ans = 100_000
# cnt = 0
# for i in data:
#     if i == 'D':
#         cnt += 1
#     elif cnt != 0:
#         ans = min(ans, cnt)
#         cnt = 0
#
# if cnt != 0: ans = min(ans, cnt)
# print(ans)

##################

# for i in 'ABCEF' : data = data.replace(i, ' ')
#
# data = data.split()
# print(len(min(data, key=len)))

pattern = r'D+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(min(matches, key=len)))