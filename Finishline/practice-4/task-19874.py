def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(10, 10_000):
    R = convert(N, 3)
    if N % 4 == 0:
        R = R + R[-3:]
    else:
        R = '1' + R + '20'
    R = int(R, 3)
    if R > 423:
        ans.append(R)

print(min(ans))