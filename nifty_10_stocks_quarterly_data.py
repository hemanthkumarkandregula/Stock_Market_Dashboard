import yfinance as yf
import pandas as pd

# List of Nifty 50 stock symbols (sample 10)
nifty_50_stocks = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'BHARTIARTL.NS', 'ICICIBANK.NS',
    'SBIN.NS', 'INFY.NS', 'BAJFINANCE.NS', 'HINDUNILVR.NS', 'ITC.NS'
]

quarterly_data = []

# Get quarter and fiscal year
def get_quarter_and_fiscal_year(date):
    m = date.month
    y = date.year
    if m in [4, 5, 6]:
        return "Q1", y
    elif m in [7, 8, 9]:
        return "Q2", y
    elif m in [10, 11, 12]:
        return "Q3", y
    else:
        return "Q4", y - 1

for stock in nifty_50_stocks:
    stock_info = yf.Ticker(stock)
    history = stock_info.history(period="5y")
    years_needed = sorted({d.year for d in history.index}, reverse=True)[:5]
    earnings = stock_info.quarterly_financials

    if not earnings.empty:
        for col in earnings.columns:
            q, y = get_quarter_and_fiscal_year(col)
            if y in years_needed:
                data = earnings[col]
                sales = data.get('Total Revenue') or data.get('Revenue', 'N/A')
                op_profit = data.get('Operating Income', 'N/A')
                net_profit = data.get('Net Income', 'N/A')

                quarterly_data.append({
                    'Fiscal Year': str(y),
                    'Quarter': q,
                    'Stock Name': stock.split('.')[0],
                    'Stock Symbol': stock,
                    'Sales (Total Revenue)': sales,
                    'Operating Profit': op_profit,
                    'Net Profit': net_profit
                })

df_quarters = pd.DataFrame(quarterly_data)
df_quarters.to_csv('nifty_10_stocks_quarterly_data.csv', index=False)

print("CSV created with Sales, Operating Profit, and Net Profit for each quarter in the last 5 years!")
