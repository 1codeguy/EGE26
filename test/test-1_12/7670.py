ans = []
for N in range(151, 100_000):
    R = hex(N)[2:]
    new_R = ''
    for i in R:
        if i == 'a':
            new_R += '1'
        else:
            new_R += i
    R = new_R
    cnt = 0
    for i in R:
        if int(i, 16) % 2 == 0:
            cnt += 1
    if cnt > 2:
        R = R + 'b'
    else:
        R = 'f' + R
    R = int(R, 16)
    if R > 3500:
        ans.append([R, N])
print(min(ans))

