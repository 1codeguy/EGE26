num = 15*49**237 + 37*343**500 - 14*7**35

cnt = 0
while num:
    if num % 49 > 15:
        cnt += 1
    num //= 49

print(cnt)