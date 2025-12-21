from string import ascii_uppercase, digits
from re import finditer

with open(r'/Users/admin/Desktop/N24/24_21421.txt') as file:
    data = file.readline()

# alph = '0123456789AB'
# alph_chet = '02468A'
# ans = 0
# i = 0
# while i < (len(data)):
#     if data[i] in alph and data[i] != '0' :
#         cnt = 1
#         for j in range(i + 1, len(data)):
#             if data[j] in alph:
#                 cnt += 1
#                 if data[j] in alph_chet:
#                     ans = max(ans, cnt)
#             else:
#                 i = j
#                 break
#     i += 1
# print(ans)

####################

# alph = '0123456789AB'
# alph_chet = '02468A'
# for i in ascii_uppercase + digits:
#     if i not in alph:
#         data = data.replace(i, ' ')
#
# data = data.split()
#
# ans = 0
# for num in data:
#      num = num.lstrip('0')
#      if num and num[-1] in alph_chet:
#          ans = max(ans, len(num))
#      else:
#          while num and num[-1] not in alph_chet:
#              num = num[:-1]
#          if num:
#              ans = max(ans, len(num))
# print(ans)

####################

pattern = r'[1-9AB][0-9AB]*[02468A]'
matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))