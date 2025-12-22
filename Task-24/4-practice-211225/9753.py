from re import finditer
with open(r'/Users/admin/Desktop/N24/24_9753.txt') as file:
    data = file.readline()

# ans = 0
# for i in range(len(data)):
#     cnt = 0
#     cnt_Y = 0
#     for j in range(i, len(data)):
#         if data[j] == 'Y':
#             cnt_Y += 1
#         if cnt_Y == 151:
#             break
#         cnt += 1
#     if cnt_Y == 151:
#         ans = max(ans, cnt)
#
# print(ans)

##########################

# data = data.split('Y')
# ans = 0
# for i in range(len(data) - 150):
#     text = 'Y'.join(data[i:i+151])
#     ans = max(ans, len(text))
# print(ans)

##########################

pattern = r'(^|(?<=Y))([^Y]*Y){150}[^Y]*($|(?=Y))'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))