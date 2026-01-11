from string import printable as skinhead

def convert(num, sys):
    res = ''
    while num:
        res += skinhead[num % sys]
        num //= sys
    return res[::-1]

ans = []
for n in range(1, 100_000):
    r = convert(n, 7)
    if r[-1] == 2:
        for i in r:
            r = r.replace('1', '*')
            r = r.replace('3', '1')
            r = r.replace('*', '3')
        r = '21' + r
    else:
        r = '1' + r[1:] + '36'
    r = int(r, 7)
    if r == 664:
        print(n)
        break

# print(max(ans))