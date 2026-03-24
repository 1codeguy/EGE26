def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 5)
    if sum(map(int, R)) % 5 == 0:
        R = R.replace('1', '*')
        R = R.replace('0', '1')
        R = R.replace('*', '0')
        R = R + '14'
    else:
        R = '44' + R[2:] + '33'
    R = int(R, 5)
    if R > 370:
        ans.append([R, N])

print(min(ans))