stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

stock_symbol = input("Please enter the stock symbol: ")
date1 = input("Please enter the first date (YYYY-MM-DD): ")
date2 = input("Please enter the second date (YYYY-MM-DD): ")

def average_price(stock_data, stock_symbol, date1, date2):
    total_price = 0
    count = 0

    for symbol, stock_date, price in stock_data:
        if symbol == stock_symbol and date1 <= stock_date <= date2:
            total_price += price
            count += 1

    if count == 0:
        return None 
    else:
        return total_price / count

average = average_price(stock_data, stock_symbol, date1, date2)
print(f"Average price for {stock_symbol} between {date1} and {date2}: ${average:.2f}")
