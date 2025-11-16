ans = []

for n in range(3, 100_000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r[:4] + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r > 600:
        ans.append(r)

print(min(ans))
