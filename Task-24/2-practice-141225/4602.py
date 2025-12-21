from string import ascii_uppercase
from re import *

with open(r'/Users/admin/Desktop/N24/24_4602.txt') as file:
    data = file.read()

# combinations = []
# vowels = 'EYUIOA'
# for i in ascii_uppercase:
#     for j in vowels:
#         if i not in vowels:
#             combinations.append(i + j)
#
# ans = 0
# for i in range(len(data) - 1):
#     if data[i] + data[i + 1] in combinations:
#         cnt = 1
#         for j in range(i + 2, len(data) - 1, 2):
#             if data[j] + data[j + 1] in combinations:
#                 cnt += 1
#             else:
#                 break
#         ans = max(ans, cnt)
#
# print(ans)

#####################

# vowels = 'EYUIOA'
# for i in ascii_uppercase:
#     if i in vowels:
#         data = data.replace(i, '*')
#     else:
#         data = data.replace(i, '+')
#
# data = data.replace('+*', '!')
# data = data.replace('+', ' ')
# data = data.replace('*', ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

#####################

vowels = 'EYUIOA'
pattern = fr'([BCD][AO])+'
matches = [match.group() for match in finditer(pattern, data)]

print(len(max(matches, key=len)) // 2)
