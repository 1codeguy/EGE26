from string import printable as skinhead

def most_num(data):
    most = []
    for i in data:
        most.append([data.count(i), i])
    return int(max(most)[1])

google = 0
for x in skinhead[1:35]:
    num1 = int(f'6{x}QR{x}', 35)
    num2 = int(f'{x}59SH', 35)
    num3 = int(f'PH{x}69YW', 35)
    num = num1 + num2 + num3
    most = most_num(str(num))
    if num % (most ** 2) == 0:
        google = num // most ** 2

print(google)
