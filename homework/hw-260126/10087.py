ans = []

for n in range(1, 100_000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin(n % 3 * 3)[2:]
    r = int(r, 2)
    if r > 151:
        ans.append(r)

print(min(ans))