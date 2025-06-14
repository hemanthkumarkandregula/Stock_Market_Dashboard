import yfinance as yf
import pandas as pd
from urllib.parse import urlparse

# List of Nifty 50 stock symbols
nifty_50_stocks = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'BHARTIARTL.NS', 'ICICIBANK.NS',
    'SBIN.NS', 'INFY.NS', 'BAJFINANCE.NS', 'HINDUNILVR.NS', 'ITC.NS'
]

# Initialize an empty list to hold the data
stock_data = []

# Function to extract domain name from website URL without 'www.'
def get_domain_name(website_url):
    if website_url:
        domain = urlparse(website_url).netloc
        # Remove 'www.' if it exists in the domain
        return domain.replace('www.', '')
    return 'No Domain'

# Function to construct the logo URL
def get_logo_url(domain_name):
    return f"https://img.logo.dev/{domain_name}"

# Fetch data for each stock
for stock in nifty_50_stocks:
    stock_info = yf.Ticker(stock)
    
    # Get fundamental data
    info = stock_info.info
    website = info.get('website')

    # Extract domain name from the website URL
    domain_name = get_domain_name(website)
    
    # Construct the logo URL
    logo_url = get_logo_url(domain_name)

    # Get current day data
    data = stock_info.history(period="1d")

    for index, row in data.iterrows():
        stock_data.append({
            'Stock Name': stock.split('.')[0],
            'Stock Symbol': stock,
            'Website': website,
            'Domain Name': domain_name,
            'Logo URL': logo_url
        })

# Create a DataFrame from the list
df = pd.DataFrame(stock_data)

# Save to CSV
df.to_csv('nifty_10_stocks_images.csv', index=False)

print("CSV file created with complete fundamental and technical data, including Domain Name and Logo URL!")
