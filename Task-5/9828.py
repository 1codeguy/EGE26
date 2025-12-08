def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []

for n in range(1, 100_000):
    r = convert(n, 3)
    if n % 3 == 0:
        r = '1' + r + '02'
    else:
        r = r + convert((n % 3) * 4, 3)
    r = int(r, 3)
    if r < 199:
        ans.append(n)
print(max(ans))
