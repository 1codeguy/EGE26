with open(r'/Users/admin/Desktop/N24/24-371.txt') as file:
    data = file.readline()

pos_M = [i for i in range(len(data)) if data[i] == 'M']

ans = 10 ** 10
for start, end in zip(pos_M, pos_M[112:]):
    ans = min(ans, end - start + 1)

print(ans)