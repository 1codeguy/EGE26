from re import finditer

with open(r'/Users/admin/Desktop/24_10105.txt') as file:
    data = file.readline()

# ans = 0
# for i in range(len(data)):
#     cnt = 0
#     cnt_T = 0
#     for j in range(i, len(data)):
#         if data[j] == 'T':
#             cnt_T += 1
#         if cnt_T == 100:
#             break
#         cnt += 1
#     if cnt_T == 100:
#         ans = max(ans, cnt)
#
# print(ans)

#########################

data = data.split('T')

ans = 0
for i in range(len(data) - 100):
    text = 'T'.join(data[i:i+101])
    ans = max(ans, len(text))
print(ans)

data = '***T***T****T**T***'
pattern = r'(?<=T)[^T]*T[^T]*(?=T)'

matches = [match.group() for match in finditer(pattern, data)]

print(matches)
print(len(max(matches, key=len)))