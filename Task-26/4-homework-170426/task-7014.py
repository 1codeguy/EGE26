with open(r'/Users/admin/Desktop/N26/26_7014.txt') as file:
    N = int(file.readline())
    prices = [int(i) for i in file]

max_earning_per_day = 0
sum_earning = 0

while prices:
    max_price = max(prices)
    pos = len(prices) - prices[::-1].index(max_price)
    earning_per_day = max_price * (pos + 1)
    sum_earning += earning_per_day
    max_earning_per_day = max(earning_per_day, max_earning_per_day)
    prices = prices[pos + 1:]

print(sum_earning, max_earning_per_day)

