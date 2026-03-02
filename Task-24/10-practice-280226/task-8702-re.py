from re import finditer

with open(r'/Users/admin/Desktop/N24/24-367.txt') as file:
    data = file.readline()

data = data.replace('.A', ' .A')
data = data.split()

if data[0][:2] != '.A':
    data = data[1:]

if data[-1].count('.') < 2:
    data = data[:-1]

ans = 10 ** 20
for i in range(len(data) - 599):
    line = data[i:i+599]
    line = ''.join(line)
    last = data[i + 599]
    if last.count('.') == 1:
        line += last + '.'
    else:
        pos_dot = last.find('.', 1)
        line += last[:pos_dot + 1]
    ans = min(ans, len(line))

print(ans)

# patter = r'(\.A[^.]*\..*?){600,}'
# matches = [match.group() for match in finditer(patter, data)]
# print(len(min(matches, key=len)))