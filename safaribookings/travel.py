
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json

service = Service('/usr/bin/chromedriver')


driver = webdriver.Chrome(service=service)

pages = list(range(35, 60))

value_y = 166

for page in pages:

    url = f'https://www.safaribookings.com/operators/kenya/page/{page}'

    driver.get(url)

    driver.maximize_window

    # Scroll the page down
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new tweets to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Get the page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract tweet text (adjust selectors if necessary)
    offers = soup.find_all('div', class_='col col-12 col-t-9 col-w-9')
    for offer in offers:
        print(offer.get_text())

    file = open('safaribookings.txt', 'a+')

    y = value_y
    for offer in offers:
        y+=1
        file.write(offer.get_text()+'\n')
        file.write(f'==============={y}\n')

    value_y = y

    file.close()

    print('iteration complete')

driver.quit()

