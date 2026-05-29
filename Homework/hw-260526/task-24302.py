def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    if sum(map(int, R)) % 9 == 0:
        R = R + '2'
    else:
        R = R + convert(sum(map(int, R)) % 9, 3)
    R = int(R, 3)
    if N > 166:
        ans.append(R)

print(min(ans))