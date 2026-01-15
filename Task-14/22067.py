from string import printable as nest

def convert(num, sys):
    res = ''
    while num:
        res += nest[num % sys]
        num //= sys
    return res[::-1]

num = convert(3*17**777 + 15*17**250 - 6*17**100 + 2, 17)

ans = []
for i in num:
    if i in '02468aceg':
        ans.append(i)

print(len(set(ans)))



