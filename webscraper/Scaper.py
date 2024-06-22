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
import time
import csv


def get_stock_indicators(driver):
    button_class = "button-vll9ujXF"
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[20]/div/button")))
    button.click()

    # Now we need to save the elements we want to scrape to our csv
    #Oscillators
    indicators = []
    time.sleep(5)
    elements = driver.find_elements(By.CSS_SELECTOR, ".cell-hvDpy38G.largePadding-hvDpy38G")

    # indicators saved in csv
    with open('webscraper/indicators.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
    
        # Optionally write headers to the CSV file
        # writer.writerow(["Header1", "Header2", "Header3"])
        
        # Loop through elements in steps of 3 and write to the CSV file
        for i in range(0, len(elements), 3):
            # Assuming elements[i], elements[i+1], and elements[i+2] exist
            writer.writerow([elements[i].text, elements[i+1].text, elements[i+2].text])




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
    
    # You can also interact with the website, click buttons, fill forms, etc.
    # button = driver.find_element(By.ID, 'submit-button')
    # button.click()
    time.sleep(20)
    # Always remember to close the driver after you're done
    driver.quit()

scrape("AAPL")