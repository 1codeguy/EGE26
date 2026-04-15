with open(r'/Users/admin/Desktop/26_15341.txt') as file:
    N = int(file.readline())
    cakes = [int(i) for i in file]

cakes = sorted(cakes, reverse=True)
ans = [cakes[0]]

for cake in cakes[1:]:
    if ans[-1] - cake >= 8:
        ans += [cake]

print(len(ans), ans[-1])