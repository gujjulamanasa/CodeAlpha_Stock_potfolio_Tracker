# Stock Portfolio Tracker

# 1. Define stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

total_investment = 0

# 2. Ask how many different stocks the user wants
number_of_stocks = int(input("How many stocks do you want to enter? "))

# 3. Get stock name and quantity
for i in range(number_of_stocks):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # 4. Check whether stock exists
    if stock in stock_prices:
        price = stock_prices[stock]

        # Calculate investment for this stock
        investment = price * quantity

        print("Stock price:", price)
        print("Investment:", investment)

        # Add to total
        total_investment += investment
    else:
        print("Stock not available.")

# 5. Display total
print("----------------------------")
print("Total Investment:", total_investment)
print("----------------------------")