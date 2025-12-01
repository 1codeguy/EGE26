from string import printable

def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]

num = 15*343**2031 + 7*49**1142 + 3*7**111 + 7**222 - 16809
num = convert(num, 7)
cnt_ch = 0
cnt_nch = 0
for i in num:
    if int(i) % 2 == 0:
        cnt_ch += 1
    else:
        cnt_nch += 1

ans = cnt_ch - cnt_nch
print(ans)