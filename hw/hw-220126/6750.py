def f(x):
    for x in range(1, 1000):
        for y in range(1, 1000):
            F = (x + y <= 32) or (y <= x + 4) or (y >= A)
            if not F:
                return False
    return True

ans = []
for A in range(1000):
    if f(A):
        ans.append(A)

print(max(ans))