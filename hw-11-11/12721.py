def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []

for n in range(1, 100_000):
    k = 0
    r = convert(n, 8)
    while r != 0:
        if map(int, r) % 2 != 0:
            k += 1
            l = int(r, 8)
            int(r, 8) //= 8
    if k % 2 == 0:
        r = r + '46'
    else:
        r = convert((r % 8) * 5, 8) + r
    r = int(r, 8)
    if n >= 80:
        ans.append(r)

print(min(ans))



