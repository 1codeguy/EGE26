from string import printable as sad

def convert(num, sys):
    res = ''
    while num:
        res += sad[num % sys]
        num //= sys
    return res[::-1]

ans = []
for N in range(1, 100_000):
    R = convert(N, 5)
    new_R = ''
    if R[-1] == '0':
        for i in R:
            if i == '1':
                new_R += '4'
            elif i == '4':
                new_R += '1'
            else:
                new_R += i
        new_R = '33' + new_R
        R = new_R
    else:
        R = '3' + R[1:] + '42'
    R = int(R, 5)
    if R < 1922:
        ans.append([R, N])

all_n = []
max_R = max(ans)[0]
for i in ans:
    if max_R == i[0]:
        all_n.append(i[1])

print(min(all_n))