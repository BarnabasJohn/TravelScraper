
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json
from tours import tours
'''
service = Service('/usr/bin/chromedriver')


driver = webdriver.Chrome(service=service)

details = {
    "description": "col-lg-8",
    "price": "object-price mr-4",
    "overview" : "col-lg-4 push-lg-2 pr-5",
    "inclusions" : "row lead"
}

for key, value in tours.items():

    url = f'https://www.fourbrothersadventures.co.ke/{value}'

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

    # Extract description text (adjust selectors if necessary)
    descriptions = soup.find_all('div', class_=f'{details["description"]}')
    for description in descriptions:
        info[detail_keys[0]] = {}
        info[detail_keys[0]] = description.get_text()
        print(description.get_text())

    # Extract price text (adjust selectors if necessary)
    prices = soup.find_all('span', class_=f'{details["price"]}')
    for price in prices:
        info[detail_keys[1]] = {}
        info[detail_keys[1]] = price.get_text()
        print(price.get_text())

    # Extract overview text (adjust selectors if necessary)
    overviews = soup.find_all('div', class_=f'{details["overview"]}')
    for overview in overviews:
        info[detail_keys[2]] = {}
        info[detail_keys[2]] = overview.get_text()
        print(overview.get_text())

    # Extract inclusion text (adjust selectors if necessary)
    inclusions = soup.find_all('div', class_=f'{details["inclusions"]}')
    for inclusion in inclusions:
        info[detail_keys[3]] = {}
        info[detail_keys[3]] = inclusion.get_text()
        print(inclusion.get_text())

    with open(f'brothers/{key}.json', 'w') as json_file:
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
    with open(f'brothers/{key}.json', 'r') as json_file:
        data = json.load(json_file)

    # Step 2: Clean the data (remove a given space sequence)
    space_sequence = "      "  # For example, removing 6 consecutive spaces
    cleaned_data = clean_spaces(data, space_sequence)

    # Step 3: Write the cleaned data to a new JSON file
    with open(f'brothers/{key}.json', 'w') as cleaned_file:
        json.dump(cleaned_data, cleaned_file, indent=4)

    print("Specific space, newline and tab characters removed successfully!")

'''
for key, value in tours.items():
    def clean_spaces(data, space_sequence):
        if isinstance(data, dict):
            return {key: clean_spaces(value, space_sequence) for key, value in data.items()}
        elif isinstance(data, list):
            return [clean_spaces(item, space_sequence) for item in data]
        elif isinstance(data, str):
            # Remove the given sequence of spaces from strings
            return data.replace(space_sequence, '').replace('\u2019s', '')
        else:
            return data

    # Step 1: Read the JSON file
    with open(f'brothers/{key}.json', 'r') as json_file:
        data = json.load(json_file)

    # Step 2: Clean the data (remove a given space sequence)
    space_sequence = "  "  # For example, removing 6 consecutive spaces
    cleaned_data = clean_spaces(data, space_sequence)

    # Step 3: Write the cleaned data to a new JSON file
    with open(f'brothers/{key}.json', 'w') as cleaned_file:
        json.dump(cleaned_data, cleaned_file, indent=4)

    print("Specific space characters removed successfully!")
