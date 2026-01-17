with open(r'/Users/admin/Desktop/N24/24_20909.txt') as file:
    data = file.readline()

# ans = 0
# for i in range(len(data)):
#     cnt = 0
#     cnt_AB = 0
#     for j in range(i, len(data) - 1, 2):
#         if data[j] + data[j + 1] == 'AB':
#             cnt_AB += 1
#         if cnt_AB == 100:
#             break
#         cnt += 2
#     if cnt_AB == 100:
#         ans = max(ans, cnt)
# print(ans)

data = data.split('AB')

ans = 0
for i in range(len(data) - 100):
    if i == 0 or i == len(data) - 101:
        text = 'AB'.join(data[i:i+101])
        ans = max(ans, len(text) + 1)
    else:
        text = 'AB'.join(data[i:i + 101])
        ans = max(ans, len(text) + 2)
print(ans)
