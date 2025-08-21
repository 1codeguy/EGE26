num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
if num1 <= 8 and num2 <= 8 and num3 <= 8 and num4 <= 8:
    if num1 - num2 == 2 and num3 - num4 == 1 or \
        num1 - num2 == 1  and num3 - num4 == 2:
        print("YES")
    elif num2 - num1 == 2 and num4 - num3 == 1 or \
        num2 - num1 == 1  and num4 - num3 == 2:
        print("YES")
    else:
        print("NO")
else:
    print('ERROR')
