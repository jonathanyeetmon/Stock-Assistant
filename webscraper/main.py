from scraper import scrape
from preprocess import pre_process

ticker = input("Enter a ticker: ")
ticker = pre_process(ticker)
scrape(ticker)