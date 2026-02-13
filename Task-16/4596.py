def F(n):
    if n < 3: return 1
    if n > 2 and n % 2 == 0: return F(n - 1) + n - 1
    return F(n - 2) + 2 * n - 2

print(F(34))