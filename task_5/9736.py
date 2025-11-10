new_r = 0
for n in range(1,100_000):
    r = bin(n)[2:]
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        r = r + bin((n % 3) * 3)[2:]
    r = int(r, 2)
    if r <= 170 and r > new_r:
        new_r = r

print(new_r)