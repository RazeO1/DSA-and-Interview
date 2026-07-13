def solve(prices):
    profit = 0

    for i in range(1, len(prices)):
        profit += max(0, prices[i] - prices[i - 1])

    print(profit)

if __name__ == "__main__":
    prices = list(map(int, input().split()))
    solve(prices)