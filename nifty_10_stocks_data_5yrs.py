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
    
    # Get fundamental data
    info = stock_info.info
    market_cap = info.get('marketCap')
    pe_ratio = info.get('trailingPE')
    eps = info.get('trailingEps')
    fifty_two_week_high = info.get('fiftyTwoWeekHigh')
    fifty_two_week_low = info.get('fiftyTwoWeekLow')
    current_price = info.get('currentPrice')  # Get current market price
    
    # Get historical stock data for the past 5 years
    data = stock_info.history(period="5y")

    # Append the relevant data to the list
    for index, row in data.iterrows():
        stock_data.append({
            'Date': index.date(),
            'Stock Name': stock.split('.')[0],
            'Stock Symbol': stock,
            'Open': row['Open'],
            'High': row['High'],
            'Low': row['Low'],
            'Close': row['Close'],
            'Volume': row['Volume'],
        })

# Create a DataFrame from the list
df = pd.DataFrame(stock_data)

# Save the DataFrame to a CSV file
df.to_csv('nifty_10_stocks_data_5yrs.csv', index=False)

print("CSV file created with Market Cap, P/E Ratio, EPS, 52W High/Low, Dividend Yield, ROE, and CMP!")
