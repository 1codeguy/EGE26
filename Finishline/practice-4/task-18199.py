def f(x, y, s):
    if x + y >= 77: return s % 2 == 0
    if s == 0: return 0
    h = [f(x + 3, y, s - 1),
         f(x * 3, y, s - 1),
         f(x, y + 3, s - 1),
         f(x, y * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else any(h)

# print('19)', min(i for i in range(1, 65) if f(i, 12, 2))) #21
print('20)', [i for i in range(1, 65) if f(i, 12, 3) and not f(i, 12, 1)])
print('21)', min(i for i in range(1, 65) if f(i, 12, 4) and not f(i, 12, 2)))