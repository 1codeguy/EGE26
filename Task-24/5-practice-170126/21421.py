from re import finditer
from string import ascii_uppercase, digits

with open(r'/Users/admin/Desktop/N24/24_21421.txt') as file:
    data = file.readline()

# pattern = r'[1-9AB][0-9AB]*[02468A]'
# matches = [match.group() for match in finditer(pattern, data)]
# print(len(max(matches, key=len)))

#################

# alph = digits + ascii_uppercase
#
# for i in alph[12:]:
#     data = data.replace(i, ' ')
#
# data = data.split()
#
# ans = 0
# for i in data:
#     ans = max(ans, len(i.lstrip('0').rstrip(alph[1:12:2])))
#
# print(ans)

##################

alph = digits + ascii_uppercase

ans = 0
for i in range(len(data)):
    if data[i] in alph[1:12]:
        cnt = 1
        for j in range(i + 1, len(data)):
            if data[j] in alph[:12]:
                cnt += 1
                if data[j] in alph[:12:2]:
                    ans = max(ans, cnt)
            else:
                break

print(ans)


