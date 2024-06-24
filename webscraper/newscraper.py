from gnews import GNews

def backtest_scrape_news_data(ticker, start_date, end_date):
    google_news = GNews()
    google_news.start_date = start_date
    google_news.end_date = end_date
    google_news.max_results = 50  # number of responses across a keyword
    google_news.country = 'United States'  # News from a specific country 
    google_news.language = 'english'  # News in a specific language
    json_news = google_news.get_news(ticker)
    descriptions = [article['description'] for article in json_news]
    return descriptions

def scrape_news_data(ticker):
    google_news = GNews()
    google_news.period = '7d'  # News from last 7 days
    google_news.max_results = 50  # number of responses across a keyword
    google_news.country = 'United States'  # News from a specific country 
    google_news.language = 'english'  # News in a specific language
    #google_news.exclude_websites = ['yahoo.com', 'cnn.com']  # Exclude news from specific website i.e Yahoo.com and CNN.com    
    json_news = google_news.get_news(ticker)
    descriptions = [article['description'] for article in json_news]
    return descriptions