days, variance = map(int, input().split())
prices = list(map(int, input().split()))

benefit = 0

for i in range(days - 1):
    for j in range(i + 1, min(i + variance + 1, days)):
        if (prices[j] - prices[i] > benefit):
            benefit = prices[j] - prices[i]

print(benefit)