with open(r'/Users/admin/Desktop/N24/24_19967.txt') as file:
    data = file.readline()

data = data.replace('AFD', '#')
data = data.replace('*', '+')
for i in '12345678':
    data = data.replace(i, '9')
for i in 'ABCDEF':
    data = data.replace(i, ' ')

data = data.replace('#09', '# 09')
data = data.replace('#00', '# 00')
data = data.replace('#+', '# +')
data = data.replace('#', ' #')

data = data.replace('++', '+ +')
data = data.replace('+09', '+0 9')

data = data.split()
ans = 0
for i in data:
    if i[0] == '#':
        i = i.rstrip('+')
        ans = max(ans, len(i) + 2)
print(ans)
