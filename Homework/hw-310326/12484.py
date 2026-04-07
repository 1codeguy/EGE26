def convert(num, sys):
    res = ''
    while num != 0:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []

for x in range(1, 50):
    for y in range(1, 50):
        num = 5**50 + 5**30 - 5**x - y - 5**y - x
        if convert(num, 5).count('0') == 10:
            ans.append(x * y)

print(max(ans))
