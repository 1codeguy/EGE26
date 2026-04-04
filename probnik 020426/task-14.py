ans = 0

for x in range(1, 9431):
    num = 39**483 + 39**235 - x
    res = ''
    while num >= 39:
        if 0 <= num % 39 <= 9:
            res += str(num % 39)
        num //= 39
    ans = max(ans, res.count('0'))

print(ans)