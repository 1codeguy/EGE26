cnt = 0
for k in range(1, 16):
    for p in range(k):
        for b in range(p):
            if k + p + b <= 15:
                cnt += 1
print(cnt)