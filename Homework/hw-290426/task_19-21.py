def f(x, y, s):
    if x + y >= 154: return s % 2 == 0
    if s == 0: return 0
    h = [f(x + 4, y, s - 1),
         f(x * 3, y, s - 1),
         f(x, y + 4, s - 1),
         f(x, y * 3, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else all(h)

# print('19)', *[x for x in range(1, 143) if f(x, 11, 2)]) 16
print('20)', *[x for x in range(1, 143) if f(x, 11, 3) and not f(x, 11, 1)][:2])
print('21)', min(x for x in range(1, 143) if f(x, 11, 4) and not f(x, 11, 2)))
