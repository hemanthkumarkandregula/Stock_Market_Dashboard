import yfinance as yf
import pandas as pd

# List of valid NIFTY index symbols for Yahoo Finance along with their names
nifty_indices = [
    {'symbol': '^NSEI', 'name': 'Nifty 50'},
    {'symbol': '^NSEBANK', 'name': 'Nifty Bank'},
    {'symbol': '^CNXIT', 'name': 'Nifty IT'},
    {'symbol': '^CNXAUTO', 'name': 'Nifty Auto'},
    {'symbol': '^CNXENERGY', 'name': 'Nifty Energy'},
    {'symbol': '^CNXMETAL', 'name': 'Nifty Metal'},
    {'symbol': '^CNXPHARMA', 'name': 'Nifty Pharma'},
    {'symbol': '^CNXREALTY', 'name': 'Nifty Realty'},
    {'symbol': '^NSEMDCP50', 'name': 'Nifty Midcap 50'},
    {'symbol': '^NSE100', 'name': 'Nifty 100'},
    {'symbol': '^NSELDCP50', 'name': 'Nifty LargeCap 50'},
    {'symbol': '^CNXFMCG', 'name': 'Nifty FMCG'},
    {'symbol': '^CNXFIN', 'name': 'Nifty Financial Services'},
]

# Initialize an empty list to hold the data
index_data = []

# Fetch data for each index
for index in nifty_indices:
    symbol = index['symbol']
    name = index['name']
    
    index_info = yf.Ticker(symbol)
    
    try:
        data = index_info.history(period="2d").tail(2)
        
        if not data.empty and len(data) >= 2:
            dates = data.index
            values = data[['Close']].values
            
            previous_close = values[0][0]
            current_price = values[1][0]
            percent_change = ((current_price - previous_close) / previous_close) * 100
            percent_change_rounded = round(percent_change, 2)

            # Determine arrow based on change
            if percent_change_rounded > 0:
                change_symbol = "▲+"
            elif percent_change_rounded < 0:
                change_symbol = "▼"
            else:
                change_symbol = "➖"
            
            index_data.append({
                'Date': dates[1].date(),
                'Index Symbol': symbol,
                'Index Name': name,
                'Current Price': round(current_price, 2),
                'Previous Close': round(previous_close, 2),
                'Change %': f"{change_symbol}{percent_change_rounded}%"
            })
        else:
            print(f"No data available for {symbol}")
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Create a DataFrame
df = pd.DataFrame(index_data)

# Save to CSV
df.to_csv('nifty_indices_daily_data.csv', index=False)

print("CSV file created with Index Symbol, Index Name, Current Price, Previous Close, Change %, and Date!")
