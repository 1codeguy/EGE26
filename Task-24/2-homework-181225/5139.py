from re import*

with open(r'/Users/admin/Desktop/N24/24_5139.txt') as file:
    data = file.readline()

# vowels = ['A', 'E', 'U']
# consonants = ['B', 'C', 'D', 'F']

# cnt = 0
# ans = 0
# for i in range(len(data) - 2):
#     if data[i] in consonants and data[i + 1] in vowels and data[i + 2] in consonants:
#         cnt = 1
#         for j in range(i + 3, len(data) - 2, 3):
#             if data[j] in consonants and data[j + 1] in vowels and data[j + 2] in consonants:
#                 cnt += 1
#             else:
#                 break
#         ans = max(ans, cnt)
#
# print(ans)

###################

# vowels = ['A', 'E', 'U']
# consonants = ['B', 'C', 'D', 'F']
# for i in data:
#     if i in vowels:
#         data = data.replace(i, '*')
#     else:
#         data = data.replace(i, '+')
#
# data = data.replace('+*+', '!')
# data = data.replace('*', ' ')
# data = data.replace('+', ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

###################
vow = '[AUE]'
con = '[BCDF]'
pattern = fr'({con}{vow}{con})+'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)) // 3)