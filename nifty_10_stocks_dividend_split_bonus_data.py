import yfinance as yf
import pandas as pd

# List of Nifty 50 stock symbols
nifty_50_stocks = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'BHARTIARTL.NS', 'ICICIBANK.NS',
    'SBIN.NS', 'INFY.NS', 'BAJFINANCE.NS', 'HINDUNILVR.NS', 'ITC.NS'
]

# Initialize an empty list to hold the data
stock_data = []

# Fetch data for each stock
for stock in nifty_50_stocks:
    stock_info = yf.Ticker(stock)
    
    # Get historical dividends and splits for the past 5 years
    dividends = stock_info.dividends
    splits = stock_info.splits

    # Create a combined index of dividend and split dates
    all_dates = dividends.index.union(splits.index).sort_values()

    # Append the relevant data to the list
    for date in all_dates:
        split_value = splits.get(date, 0.0)

        # Format split as ratio (e.g., 5.0 => 1:5)
        if split_value >= 1:
            split_ratio = "1:" + str(int(split_value))
        else:
            split_ratio = ""

        # Identify bonus based on typical 1:1 or 1:2 ratios (heuristic)
        if split_value >= 1.1 and split_value <= 2.1:
            bonus_ratio = "1:" + str(int(split_value))
        else:
            bonus_ratio = ""

        stock_data.append({
            'Date': date.date(),
            'Stock Name': stock.split('.')[0],
            'Stock Symbol': stock,
            'Dividend Amount': dividends.get(date, 0.0),
            'Split Ratio': split_ratio,
            'Bonus Ratio': bonus_ratio
        })

# Create a DataFrame from the list
df = pd.DataFrame(stock_data)

# Save the DataFrame to a CSV file
df.to_csv('nifty_10_stocks_dividend_split_bonus_data.csv', index=False)

print("CSV file created with Dividend, Split (as ratio), and Bonus (as ratio)!")
