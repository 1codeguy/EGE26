from re import *

with open(r'/Users/admin/Desktop/24_1874.txt') as file:
    data = file.readline()

# ans = 0
# cnt = 1
# for i in range(len(data) - 1):
#     if data[i] + data[i + 1] != 'QW':
#         cnt += 1
#     else:
#         ans = max(ans, cnt)
#         cnt = 1
# ans = max(ans, cnt)
#
# print(ans)

# while 'QW' in data:
#     data = data.replace('QW', 'Q W')
#
# data = data.split()
#
# print(len(max(data, key=len)))

pattern = r'(?<=QW).*?(?=QW)'
matches = [match.group() for match in finditer(pattern, data)]

print(matches)
ans_str = max(matches, key=len)
print(len(ans_str))

# print(data[pos_ans_str - 100:pos_ans_str])
# print()
# print(data[pos_ans_str:pos_ans_str + len(ans_str)])
# print()
# print(data[pos_ans_str + len(ans_str):pos_ans_str + len(ans_str) + 100])