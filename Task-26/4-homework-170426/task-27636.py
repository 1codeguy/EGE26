with open(r'/Users/admin/Desktop/N26/26_27636.txt') as file:
    N = list(map(int, file.readline().split()))
    data = [int(i) for i in file]

data = sorted(data)

for num in data:
    if N[0] - num > 0:
        N[1] = N[1] - 1
        N[0] = N[0] - num
    else:
        N[0] = N[0] - num
        N[1] -= 1
        break

print(N[0], N[1])