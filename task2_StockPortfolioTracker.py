import csv
from datetime import datetime

# Hardcoded stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330,
    "AMZN": 145,
}


def get_portfolio():
    portfolio = {}
    print("Available stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Enter stock symbol and quantity. Type 'done' to finish.\n")

    while True:
        symbol = input("Stock symbol: ").upper().strip()
        if symbol == "DONE":
            break
        if symbol not in STOCK_PRICES:
            print("Unknown stock symbol. Try again.")
            continue
        try:
            qty = int(input(f"Quantity of {symbol}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + qty

    return portfolio


def calculate_totals(portfolio):
    rows = []
    total_value = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total_value += value
        rows.append((symbol, qty, price, value))
    return rows, total_value


def save_to_csv(rows, total_value, filename="portfolio_summary.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])
        writer.writerows(rows)
        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_value])
        writer.writerow(["Generated on", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    print(f"\nSaved summary to {filename}")


def main():
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    rows, total_value = calculate_totals(portfolio)

    print("\n--- Portfolio Summary ---")
    for symbol, qty, price, value in rows:

        print(f"{symbol}: {qty} shares @ ${price} = ${value}")
    print(f"\nTotal Investment Value: ${total_value}")

    choice = input("\nSave summary to CSV? (y/n): ").lower().strip()
    if choice == "y":
        save_to_csv(rows, total_value)


if __name__ == "__main__":
    main()