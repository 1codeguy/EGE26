def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

for N in range(2, 100_000):
    R = convert(N, 3)
    if N % 3 == 0:
        R += R[-2:]
    else:
        R = R + convert(N % 3 * 3, 3)
    R = int(R, 3)
    if R <= 150:
        print(N)