import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
import os
import sys

parent_dir = os.getcwd()  # Get the current working directory

# Print the current sys.path for debugging purposes
print("Current sys.path:")
print(sys.path)

# Add the webscraper_path to sys.path if not already included
sys.path.append(parent_dir)
print("\nNew sys.path:")
print(sys.path)

# Now attempt to import from the webscraper module
try:
    from webscraper.scraper import sentiment_analysis_from_headlines
    from webscraper.newscraper import backtest_scrape_news_data
except ModuleNotFoundError as e:
    print(f"Failed to import: {e}")
    print(f"Ensure that 'webscraper' module is located at: {parent_dir}")
    sys.exit(1)

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    return df

def check_stock_performance(ticker, end_date):
    one_month_later = end_date + timedelta(days=30)
    stock = yf.Ticker(ticker)
    df = stock.history(start=end_date, end=one_month_later)
    if df.empty:
        return None
    start_price = df['Close'].iloc[0]
    end_price = df['Close'].iloc[-1]
    return "buy" if end_price > start_price else "sell"

def backtest_stock_sentiment(ticker, start_date, end_date):
    # Fetch historical stock data
    df = fetch_stock_data(ticker, start_date, end_date)
    if df.empty:
        print("No data available for the given time frame.")
        return

    # Analyze sentiment
    headlines = backtest_scrape_news_data(ticker, start_date, end_date)
    sentiment_prediction = sentiment_analysis_from_headlines(headlines)

    # Check actual stock performance
    actual_performance = check_stock_performance(ticker, end_date)

    # Compare decision with actual performance
    return sentiment_prediction, actual_performance

def calculate_score(stock_predictions):
    '''
    returns the average amount of times the model is correct 
    on backtested data when it gives a reccomendation to the user
    '''
    total_score = 0
    valid_count = 0

    for item in stock_predictions:
        if item[1] is None:
            score = 0
        elif item[1][0] == item[1][1]:
            score = 1
        else:
            score = 0
        
        total_score += score
        if item[1] is not None and item[1][0] == 'hold':
            valid_count += 1

    average_score = total_score / valid_count
    return average_score
        
def backtest_full_test():
    stocks = pd.read_csv("testing/sp500-companies.csv", header=0, encoding='utf-8')
    tickers = stocks['Ticker'].dropna().unique()
    num_test = 100
    tickers = tickers[:num_test]
    start_date = "2023-01-01"  # Example start date
    end_date = "2023-01-07"    # Example end date

    end_date = datetime.strptime(end_date, '%Y-%m-%d')  # Adjust format as per your actual date string format
    start_date = datetime.strptime(start_date, '%Y-%m-%d')

    results = [(ticker, backtest_stock_sentiment(ticker, start_date, end_date)) for ticker in tickers]
    print(results)
    print(f"The average score is: {calculate_score(results)}")

#backtest_full_test()