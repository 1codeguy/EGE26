def del_7(num):
    for i in range(17, int(num ** .5) + 1):
        if num % i == 0:
            if i % 10 == 7:
                return i
            elif num // i % 10 == 7:
                return num // i
    return 0

cnt = 0
for N in range(700_001, 10 ** 8):
    if F := del_7(N):
        print(N, F)
        cnt += 1
        if cnt == 5:
            break