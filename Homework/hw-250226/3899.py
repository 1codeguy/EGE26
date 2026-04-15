def f(cur):
    if cur == 8: return 1
    if cur < 10: return 0
    return f(cur % 10 + cur // 10) + f(cur % 10 * (cur // 10))

cnt = 0
for num in range(10, 100):
    if f(num):
        cnt += 1

print(cnt)