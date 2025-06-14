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
    current_price = info.get('currentPrice')
    sector = info.get('sector')
    industry = info.get('industry')
    beta = info.get('beta')
    previous_close = info.get('previousClose')
    volume = info.get('volume')
    avg_volume = info.get('averageVolume')
    dividend_yield = info.get('dividendYield')
    roe = info.get('returnOnEquity')
    country = info.get('country')
    currency = info.get('currency')
    book_value = info.get('bookValue')
    face_value = info.get('faceValue')
    info_summary = info.get('longBusinessSummary', 'No business summary available')

    # Additional fields
    fifty_day_avg = info.get('fiftyDayAverage')
    two_hundred_day_avg = info.get('twoHundredDayAverage')
    held_percent_insiders = info.get('heldPercentInsiders')
    held_percent_institutions = info.get('heldPercentInstitutions')
    price_to_book = info.get('priceToBook')
    enterprise_to_revenue = info.get('enterpriseToRevenue')
    enterprise_to_ebitda = info.get('enterpriseToEbitda')
    recommendation_key = info.get('recommendationKey')
    total_cash = info.get('totalCash')
    total_cash_per_share = info.get('totalCashPerShare')
    ebitda = info.get('ebitda')
    total_debt = info.get('totalDebt')
    total_revenue = info.get('totalRevenue')
    debt_to_equity = info.get('debtToEquity')
    revenue_per_share = info.get('revenuePerShare')
    gross_profits = info.get('grossProfits')
    earnings_growth = info.get('earningsGrowth')
    revenue_growth = info.get('revenueGrowth')
    gross_margins = info.get('grossMargins')
    ebitda_margins = info.get('ebitdaMargins')
    operating_margins = info.get('operatingMargins')
    analyst_rating = info.get('averageAnalystRating')
    website = info.get('website')

    # Get current day data
    data = stock_info.history(period="1d")

    for index, row in data.iterrows():
        stock_data.append({
            'Date': index.date(),
            'Stock Name': stock.split('.')[0],
            'Stock Symbol': stock,
            'Market Cap': market_cap,
            'P/E Ratio': pe_ratio,
            'EPS': eps,
            '52W High': fifty_two_week_high,
            '52W Low': fifty_two_week_low,
            'CMP': current_price,
            'Sector': sector,
            'Industry': industry,
            'Beta': beta,
            'Previous Close': previous_close,
            'Volume': volume,
            'Avg Volume': avg_volume,
            'Dividend Yield': dividend_yield,
            'ROE': roe,
            'Country': country,
            'Currency': currency,
            'Book Value': book_value,
            'Face Value': face_value,
            'Company Info': info_summary,
            '50D Avg Price': fifty_day_avg,
            '200D Avg Price': two_hundred_day_avg,
            'Held by Insiders %': held_percent_insiders,
            'Held by Institutions %': held_percent_institutions,
            'Price to Book': price_to_book,
            'Enterprise to Revenue': enterprise_to_revenue,
            'Enterprise to EBITDA': enterprise_to_ebitda,
            'Recommendation': recommendation_key,
            'Total Cash': total_cash,
            'Cash per Share': total_cash_per_share,
            'EBITDA': ebitda,
            'Total Debt': total_debt,
            'Total Revenue': total_revenue,
            'Debt to Equity': debt_to_equity,
            'Revenue per Share': revenue_per_share,
            'Gross Profits': gross_profits,
            'Earnings Growth': earnings_growth,
            'Revenue Growth': revenue_growth,
            'Gross Margins': gross_margins,
            'EBITDA Margins': ebitda_margins,
            'Operating Margins': operating_margins,
            'Avg Analyst Rating': analyst_rating,
            'Website': website
        })

# Create a DataFrame from the list
df = pd.DataFrame(stock_data)

# Save to CSV
df.to_csv('nifty_10_stocks_data_base.csv', index=False)

print("CSV file created with complete fundamental and technical data for Nifty 10 stocks!")
