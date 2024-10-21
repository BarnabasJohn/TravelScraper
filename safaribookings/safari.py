from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from park import AberdareCompanies
from bs4 import BeautifulSoup
import time
import json


service = Service('/usr/bin/chromedriver')

driver = webdriver.Chrome(service=service)

for (mkey, mvalue) in AberdareCompanies.items():

    company = {
        "overview" : {
            "url" : "tours",
            "element" : "div",
            "class" : "tour__content__block tour__content__block--accommodations avoid-break-p"
        },
        "rates" : {
            "url" : "rates",
            "element" : "table",
            "class" : "table table--sec"
        },
        "inclusions" : {
            "url" : "inclusions",
            "element" : "div",
            "class" : "tour__content__block tour__content__block--inclusions"
        },
        "gettingthere" : {
            "url" : "gettingthere",
            "element" : "div",
            "class" : "tour__content__block tour__content__block--gettingthere"
        },
    }

    company_details = {}

    for index, (key, value) in enumerate(company.items()):
        #print(f"Index {index}: Key = {key}, url = {value['url']}, element = {value['element']}, class = {value['class']}")

        url = f'https://www.safaribookings.com/{value['url']}/{mvalue}'

        driver.get(url)

        driver.maximize_window

        # Scroll the page down
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Wait for new page to load
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Get the page source and parse with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract tweet text (adjust selectors if necessary)
        offers = soup.find_all(f'{value["element"]}', class_=f'{value["class"]}')
        # for offer in offers:
        #     print(offer.get_text())

        for offer in offers:
            company_details[key] = {}
            company_details[key] = offer.get_text()

    with open(f'Aberdare2/{mkey}.json', 'w') as json_file:
            json.dump({f'{mkey}': company_details}, json_file, indent=4)

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
    with open(f'Aberdare2/{mkey}.json', 'r') as json_file:
        data = json.load(json_file)

    # Step 2: Clean the data (remove a given space sequence)
    space_sequence = "      "  # For example, removing 6 consecutive spaces
    cleaned_data = clean_spaces(data, space_sequence)

    # Step 3: Write the cleaned data to a new JSON file
    with open(f'Aberdare2/{mkey}.json', 'w') as cleaned_file:
        json.dump(cleaned_data, cleaned_file, indent=4)

    print("Specific space, newline and tab characters removed successfully!")

print("Completed sequence successfully!")