from string import printable as skinhead

def convert(num, sys):
    res = ''
    while num:
        res += skinhead[num % sys]
        num //= sys
    return res[::-1]

for N in range(1, 100_000):
    R = convert(N, 8)
    if R[0] == '5':
        R = R.replace('2', '*')
        R = R.replace('1', '2')
        R = R.replace('*', '1')
        R += '11'
    else:
        R = '2' + R[1:] + '10'
    R = int(R, 8)
    if R < 1354:
        print(N)