num = int(input())
new = ''
while num:
    new += str(num % 10)
    num //= 10
print(new)