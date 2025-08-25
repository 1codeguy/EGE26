num = int(input())
k = 0
while num > 0:
    if (num % 10) % 2 == 0:
        k += 1
    num //= 10
print(k)
