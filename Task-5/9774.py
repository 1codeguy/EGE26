def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []

for n in range(1, 100_000):
    r = convert(n,3)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + convert((n % 3) * 5, 3)
    r = int(r, 3)
    if r > 133:
        ans.append(r)
print(min(ans))




