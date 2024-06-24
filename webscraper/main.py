from .scraper import scrape
from .preprocess import pre_process

def run(ticker):
    ticker = pre_process(ticker)
    scrape(ticker)

if __name__ == "__main__":
    run()