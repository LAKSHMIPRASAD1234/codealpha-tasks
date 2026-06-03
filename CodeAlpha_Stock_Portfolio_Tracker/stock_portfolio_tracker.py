# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("================================")
print("    STOCK PORTFOLIO TRACKER")
print("================================")

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print(f"{stock_name} Investment Value: ${investment}")

print("\n================================")
print("Total Investment Value: $", total_investment)
print("================================")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio saved to portfolio.txt")