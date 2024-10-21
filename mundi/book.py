from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from tours import tours

service = Service('/usr/bin/chromedriver')

driver = webdriver.Chrome(service=service)

details = {
    "overview" : "relative inline-flex w-full shrink grow basis-0 flex-col items-start justify-start gap-2 border-b border-b-neutral-light px-0 pb-6 lg:border-0 lg:px-4 lg:py-2 lg:pb-2",
    "pricing" : "flex w-full flex-col items-end gap-1 p-0 lg:w-[240px] lg:p-2 lg:px-4 lg:pl-0"
}

for key, value in tours.items():

    url = f'https://www.bookmundi.com/o/{value}'

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
    info = {}
    detail_keys = list(details.keys())
    # Extract tweet text (adjust selectors if necessary)
    overviews = soup.find_all('div', class_=f'{details["overview"]}')
    for overview in overviews:
        info[detail_keys[0]] = {}
        info[detail_keys[0]] = overview.get_text()
        print(overview.get_text())

    # Extract tweet text (adjust selectors if necessary)
    pricings = soup.find_all('div', class_=f'{details["pricing"]}')
    for pricing in pricings:
        info[detail_keys[1]] = {}
        info[detail_keys[1]] = pricing.get_text()
        print(pricing.get_text())

    with open(f'bookm/{key}.json', 'w') as json_file:
        json.dump({f'{key}': info}, json_file, indent=4)

    def clean_spaces(data, space_sequence):
        if isinstance(data, dict):
            return {key: clean_spaces(value, space_sequence) for key, value in data.items()}
        elif isinstance(data, list):
            return [clean_spaces(item, space_sequence) for item in data]
        elif isinstance(data, str):
            # Remove the given sequence of spaces from strings
            return data.replace(space_sequence, '').replace('\n', ' ').replace('\t', '').replace('\u2013', '').replace('\u00a0', '')
        else:
            return data

    # Step 1: Read the JSON file
    with open(f'bookm/{key}.json', 'r') as json_file:
        data = json.load(json_file)

    # Step 2: Clean the data (remove a given space sequence)
    space_sequence = "      "  # For example, removing 6 consecutive spaces
    cleaned_data = clean_spaces(data, space_sequence)

    # Step 3: Write the cleaned data to a new JSON file
    with open(f'bookm/{key}.json', 'w') as cleaned_file:
        json.dump(cleaned_data, cleaned_file, indent=4)

    print("Specific space, newline and tab characters removed successfully!")

