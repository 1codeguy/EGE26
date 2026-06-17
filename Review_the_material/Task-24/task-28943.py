with open(r'files/24_28943.txt') as file:
    data = file.readline()

data = data.split('20')

ans = 10 ** 8
for i in range(len(data) - 26):
    line = '20'.join(data[i:i + 27])
    last_num_20 = line.rfind('20')
    for j in 'AEIOUY':
        line = line.replace(j, '*')
    if '*' in line[last_num_20:]:
        vow = line.index('*', last_num_20)
        line = line[:vow + 1]
        if line.count('*') == 1:
            ans = min(ans, len(line))

print(ans)