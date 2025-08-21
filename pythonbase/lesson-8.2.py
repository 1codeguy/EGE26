num = int(input())
pr = 1
while num:
    pr *= (num % 10)
    num //= 10
print(pr)