n = int(input())
num = 1
summ = 0
for i in range(n + 1):
    summ += num
    num *= -2
print(summ)