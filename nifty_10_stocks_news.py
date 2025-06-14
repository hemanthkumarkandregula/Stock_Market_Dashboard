from GoogleNews import GoogleNews
import pandas as pd

# List of Nifty 50 stock symbols
nifty_50_stocks = [
    'RELIANCE.NS', 'HDFCBANK.NS', 'TCS.NS', 'BHARTIARTL.NS', 'ICICIBANK.NS',
    'SBIN.NS', 'INFY.NS', 'BAJFINANCE.NS', 'HINDUNILVR.NS', 'ITC.NS'
]

# Initialize an empty list to hold the news data
stock_news_data = []

# Function to fetch top news articles for each stock symbol
def fetch_stock_news(stock_symbol):
    googlenews = GoogleNews(lang='en', region='IN')  # Customize the region if needed
    googlenews.search(stock_symbol)  # Search for stock-related news
    news = googlenews.results(sort=True)  # Sort news by relevance
    
    # Get the top 10 news articles
    top_news = news[:10]
    
    return top_news

# Fetch news for each stock
for stock in nifty_50_stocks:
    top_news = fetch_stock_news(stock)
    
    # Append the stock and its news to the list
    for article in top_news:
        news_data = {
            'Stock Symbol': stock.strip(),
            'News Headline': article.get('title', '').strip(),
            'Brief Summary': article.get('desc', 'No summary available').strip(),
            'Published Date': article.get('date', '').strip(),
        }
        
        # Only add news data if 'News Headline' is not empty
        if news_data['News Headline']:
            stock_news_data.append(news_data)

# Create a DataFrame from the list of news
news_df = pd.DataFrame(stock_news_data)

# Save the news data to a CSV file
news_df.to_csv('nifty_10_stocks_news.csv', index=False)

print("CSV file created with top 10 news articles for each stock!")


