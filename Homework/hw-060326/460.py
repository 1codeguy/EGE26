```
cnt = 0

for C in range(1, 2500):
    for B in range(625, 2500):
        if C + B < 3124:
            continue
    cnt += 1

print(cnt)

# 625
# 3124
```