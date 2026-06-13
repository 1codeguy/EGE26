ans = 0
for x in range(1, 9431):
    num = 39**483 + 39**235 - x
    cnt = 0
    while num:
        if num % 39 == 0:
            cnt += 1
        num //= 39
    ans = max(ans, cnt)

print(ans)