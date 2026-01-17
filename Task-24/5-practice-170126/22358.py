from re import finditer
from string import digits, ascii_uppercase

with open(r'/Users/admin/Desktop/N24/24_22358.txt') as file:
    data = file.readline()

# pattern = r'[1-9AB][0-9AB]*'
# matches = [match.group() for match in finditer(pattern, data)]
#
# ans = '0'
# for match in matches:
#     if match and int(match, 12) % 3 == 0:
#         if int(ans, 12) < int(match, 12):
#             ans = match
#     elif match:
#         for i in range(len(match)):
#             for j in range(len(match), i, -1):
#                 line = match[i:j].lstrip('0')
#                 if line and int(match, 12) % 3 == 0:
#                     if int(ans, 12) < int(line, 12):
#                         ans = line
#                         break
#
# print(data.find(ans))

###################

# alph = digits + ascii_uppercase
#
# data_2 = data
# for i in alph[12:]:
#     data_2 = data_2.replace(i, ' ')
# while ' 0' in data_2:
#     data_2 = data_2.replace(' 0', ' ')
# data_2 = data_2.split()
#
# ans = '0'
# for match in data_2:
#     if match and int(match, 12) % 3 == 0:
#         if int(ans, 12) < int(match, 12):
#             ans = match.lstrip('0')
#     elif match:
#         for i in range(len(match)):
#             for j in range(len(match), i, -1):
#                 line = match[i:j].lstrip('0')
#                 if line and int(match, 12) % 3 == 0:
#                     if int(ans, 12) < int(line, 12):
#                         ans = line
#                         break
#
# print(data.find(ans))

###############

alph = digits + ascii_uppercase

ans = '0'
for i in range(len(data)):
    if data[i] in alph[1:12]:
        num = data[i]
        for j in range(i + 1, len(data)):
            if data[j] in alph[:12]:
                num += data[j]
                if int(num, 12) % 3 == 0 and int(num, 12) % 3 == 0 > int(ans, 12):
                    ans = num
            else:
                break

print(data.find(ans))