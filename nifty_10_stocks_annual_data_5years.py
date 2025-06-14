import yfinance as yf
import pandas as pd

# List of Nifty 50 stock symbols (sample 10)
nifty_50_stocks = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'BHARTIARTL.NS', 'ICICIBANK.NS',
    'SBIN.NS', 'INFY.NS', 'BAJFINANCE.NS', 'HINDUNILVR.NS', 'ITC.NS'
]

# Initialize an empty list to hold the yearly data
yearly_data = []

# Fetch data for each stock
for stock in nifty_50_stocks:
    stock_info = yf.Ticker(stock)
    
    # Get the last 5 years of price history (for year reference)
    history = stock_info.history(period="5y")
    years_needed = sorted({d.year for d in history.index}, reverse=True)[:5]

    # Get the annual financials (income statement)
    earnings = stock_info.financials

    if earnings is not None and not earnings.empty:
        for year_col in earnings.columns:
            year = year_col.year
            if year in years_needed:
                values = earnings[year_col]
                sales = values.get('Total Revenue') or values.get('Revenue', 'N/A')
                operating_profit = values.get('Operating Income', 'N/A')
                net_profit = values.get('Net Income', 'N/A')

                yearly_data.append({
                    'Year': str(year),
                    'Stock Name': stock.split('.')[0],
                    'Stock Symbol': stock,
                    'Sales (Total Revenue)': sales,
                    'Operating Profit': operating_profit,
                    'Net Profit': net_profit
                })

# Create a DataFrame from the yearly data
df_yearly = pd.DataFrame(yearly_data)

# Save to CSV
df_yearly.to_csv('nifty_10_stocks_annual_data_5years.csv', index=False)

print("CSV created with Sales, Operating Profit, and Net Profit for the last 5 years!")
