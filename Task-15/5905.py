def f(x, y, z):
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > A // 8)

for A in range(1, 1000)[::-1]:
    if all(f(x, y, z) for x in range(1, 500) for y in range(1, 500) for z in range(1, 500)):
        print(A)
        break