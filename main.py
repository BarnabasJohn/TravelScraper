import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

service = Service('/usr/bin/chromedriver')
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(service=service, options=options)


url = 'https://x.com/MigunaMiguna'

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
tweets = soup.find_all('div', {'data-testid': 'tweet'})
for tweet in tweets:
    print(tweet.get_text())

driver.quit()

###################
#scroll down the page by pixel number
#driver.execute_script("window.scrollBy(0,900)","")
#scroll down the page till element found
#Element = driver.find_element(By.ID, '[idOfElement]')
#driver.execute_script("arguments[0].scrollIntoView();", Element)
#scroll down to end of the page
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
'''
time.sleep(5)

for _ in range(100):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(2)  # Wait for posts to load

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

#posts = soup.find_all('span', class_='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3')
#posts = soup.find_all('div', class_='css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim')
#posts = soup.find_all('div', { 'id': 'id_97mnowx9ub'})
posts = soup.find_all('div', {'data-testid':'cellInnerDiv'})
for post in posts:
    content = post.get_text()
    print(content)

'''
'''
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        headings = soup.find_all('div', {'data-testid': 'tweet'})
        #print(headings)
        if headings:
            print("found some")

            for heading in headings:
                print(heading.text.strip())
        else:
            print("failed!")
        
    except Exception as e:
        print("An exception occurred:", e)
    
else:
    print("Failed to retrieve the web page")

url = 'https://x.com/login'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:
    headings = soup.find_all('div')
    for heading in headings:
        print(heading.text.strip())
else:
    print("Failed to retrieve the web page")
'''
