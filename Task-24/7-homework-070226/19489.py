with open(r'/Users/admin/Desktop/N24/24_19489.txt') as file:
    data = file.readline()

data = data.split('WWF')

ans = 0
for i in range(len(data) - 120):
    new_line = 'WWF'.join(data[i:i+121])
    if 'WSFWW' not in new_line:
        ans = max(ans, len(new_line))
    else:
        new_line = new_line.replace('WSFWW', 'WSFW SFWW')
        new_line = new_line.split()
        ans = max(ans, len(max(new_line, key=len)))

print(ans)
