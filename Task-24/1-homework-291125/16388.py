from re import*

with open(r'/Users/admin/Desktop/24_16388.txt') as file:
    data = file.readline()

# ans = 0
# for i in range(len(data) - 3):
#     four_letters = data[i:i + 4]
#     if four_letters == 'KLMN':
#         cnt = 1
#         for j in range(i + 4, len(data), 4):
#             if data[j:j + 4] == 'KLMN':
#                 cnt += 1
#             else:
#                 break
#         cnt *= 4
#         if data[i-3:i] == 'LMN': cnt += 3
#         elif data[i-2:i] == 'MN': cnt += 2
#         elif data[i-1:i] == 'N': cnt += 1
#
#         if data[j:j+3] == 'KLM': cnt += 3
#         elif data[j:j+2] == 'KL': cnt += 2
#         elif data[j] == 'K': cnt += 1
#
#         ans = max(ans, cnt)
#
# print(ans)

# data = data.replace('KLMN', '****')
# data = data.replace('*KLM', '**** ')
# data = data.replace('*KL', '*** ')
# data = data.replace('*K', '** ')
# data = data.replace('LMN*', ' ****')
# data = data.replace('MN*', ' ***')
# data = data.replace('N*', ' **')
#
# for i in 'KLMN':
#     data = data.replace(i, ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)))