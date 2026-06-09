num = 2 * 2401**525 + 3 * 343*524 - 4 * 49*522 - 6 * 7**521 - 35

res = ''
while num >= 49:
    if 0 <= num % 49 <= 9:
        res += str(num % 49)
    num //= 49

print(res)
