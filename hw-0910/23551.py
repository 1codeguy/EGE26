ans = 0
for n in range(1, 100_000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r < 30 and n > ans:
        ans = n
print(ans)


