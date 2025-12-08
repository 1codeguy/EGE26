def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res


new_r = 2 ** 20
ans = []

for n in range(1, 100_000):
    r = convert(n, 3)
    if n % 2 == 0:
        r = r + r[-3:]
    else:
        r = r + convert(sum(map(int, r)), 3)
    r = int(r, 3)
    if r < new_r and n > 9:
        new_r = r
        ans.append(n)

print(ans)
