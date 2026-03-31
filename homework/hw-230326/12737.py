def f(x, y, s):
    if x + y >= 385: return s % 2 == 0
    if s == 0: return 0
    h = [f(x + 5, y, s - 1),
         f(x * 2, y, s - 1),
         f(x, y + 5, s - 1),
         f(x, y * 2, s - 1)]
    return any(h) if (s - 1) % 2 == 0 else any(h)

print('19)', *[x for x in range(1, 55) if f(x, 8, 2)])
# print('20)', *[x for x in range(1, 55) if f(x, 8, 3) and not f(x, 8, 1)])
# print('21)', *[x for x in range(1, 55) if f(x, 8, 4) and not f(x, 8, 2)])
