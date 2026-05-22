with open(r'./files/24_18597.txt') as file:
    data = file.readline()

data = data.split('&')

ans = 0
for num_1, num_2 in zip(data, data[1:]):
    if '.' not in num_1 or '.' not in num_2:
        continue

    dot_1 = num_1.rfind('.')
    if dot_1 < 4 or dot_1 == len(num_1) - 1 or '.' in num_1[dot_1 - 4:dot_1]:
        continue
    num_1 = num_1[dot_1 - 4:]

    dot_2 = num_2.find('.')
    if dot_2 != 4 or dot_2 == len(num_2) - 1 or num_2[dot_2 + 1] == '.':
        continue
    dot_2_2 = num_2.find('.', dot_2 + 1)
    num_2 = num_2[:dot_2_2]

    ans = max(ans, len(num_1 + '&' + num_2))

print(ans)