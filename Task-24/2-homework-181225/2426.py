from re import*

with open(r'/Users/admin/Desktop/N24/24_2426.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 0
# for i in data:
#     if i in '1 2 3':
#         cnt += 1
#     else:
#         ans = max(cnt, ans)
#         cnt = 0
#
# ans = max(cnt, ans)
#
# print(ans)

#####################

# for i in '123':
#     data = data.replace(i, '*')
#
# for i in 'ABC':
#     data = data.replace(i, ' ')
#
# data = data.split()
# print(len(max(data, key=len)))

#####################

pattern = r'\d+'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))
