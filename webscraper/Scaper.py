#Scaper.py
#Scrape Trading View For
#1. Stock Indicator Values and ratings ->everything they have lol
#2. Stock News -> Hugiging Face Sentiment Analysis of Headings
#3. Stock Price -> pretty straightforward

#importing libraries for scraper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import json


def get_stock_indicators(driver):
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[20]/div/button")))
    button.click()

    # Now we need to save the elements we want to scrape to our csv
    #Oscillators
    time.sleep(5)
    elements = driver.find_elements(By.CSS_SELECTOR, ".cell-hvDpy38G.largePadding-hvDpy38G")

    data = []
    for i in range(0, len(elements), 3):
        # Assuming elements[i], elements[i+1], and elements[i+2] exist
        # You might want to add checks to ensure you have enough elements
        group = {
            'first_element': elements[i].text,
            'second_element': elements[i + 1].text,
            'third_element': elements[i + 2].text
        }
        data.append(group)

# Writing the list of dictionaries to a JSON file
    with open('webscraper/indicators.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def get_stock_news(driver):
    time.sleep(10)
    
    


def scrape(ticker):
    # Set up the Chrome WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Go to the website you want to scrape
    url = "https://www.tradingview.com/chart/?symbol=" + ticker
    driver.get(url)

    # Now, you can find elements by their tag, class, id or other attributes

    #get stock indicators
    get_stock_indicators(driver)

    #reset back to main page so we can get the news
    url = "https://news.google.com/"
    driver.get(url)
    search_bar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".Ax4B8.ZAGvjd")))
    search_bar.send_keys(ticker)
    search_bar.send_keys(Keys.RETURN)

    #get stock news
    get_stock_news(driver)

    time.sleep(5)
    # Always remember to close the driver after you're done
    driver.quit()

scrape("AAPL")





def get_google_news(ticker):
    # Set up the Chrome driver
    service = Service('path_to_chromedriver')  # Update this with the correct path to your ChromeDriver
    driver = webdriver.Chrome(service=service)
    
    try:
        # Open Google News
        driver.get('https://news.google.com/')
        
        # Find the search box and enter the ticker
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(ticker)
        search_box.send_keys(Keys.RETURN)
        
        # Wait until the search results are loaded
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article')))
        
        # Find all articles
        articles = driver.find_elements(By.CSS_SELECTOR, 'article')
        
        # Extract the relevant information
        news_data = []
        for article in articles:
            headline_elem = article.find_element(By.CSS_SELECTOR, 'h3')
            link_elem = article.find_element(By.CSS_SELECTOR, 'a')
            snippet_elem = article.find_element(By.CSS_SELECTOR, 'p')
            
            headline = headline_elem.text if headline_elem else "No headline"
            link = link_elem.get_attribute('href') if link_elem else "No link"
            snippet = snippet_elem.text if snippet_elem else "No snippet"
            
            news_data.append({
                'headline': headline,
                'link': link,
                'snippet': snippet
            })
        
        # Convert to DataFrame
        df = pd.DataFrame(news_data)
        return df
    
    finally:
        # Close the driver
        driver.quit()
