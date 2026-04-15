def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []

for n in range(1, 100_000):
    r = convert(n, 7)
    if sum(map(int, r)) % 2 == 0:
        r = r + '555'
    else:
        r = '33' + r + '6'
    r = int(r, 7)
    if r < 12717:
        ans.append(n)

print(max(ans))
