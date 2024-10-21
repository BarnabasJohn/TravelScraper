
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import json


tours = {
    "3MaasaiMara": "3-days-masai-mara-camping-joining-safaris",
    "4MaraNakuru": "4-days-masai-mara-nakuru-camping-joining-safari-c8e3848",
    "MaraSafari": "3-days-masai-mara-safari-5f90637",
    "MNaks": "4-days-mara-nakuru-budget-safari-c8adb6d",
    "MaraPrivate": "3-days-masai-mara-private-safari-62a4355",
    "NakNaivasha": "5-days-budget-private-safari-to-maasai-mara-lake-nakuru-and-lake-naivasha-hells-gate-3d617a8",
    "AmboseliPrivate": "3-days-amboseli-private-safari-2820805",
    "6MNakAmb": "6-days-masai-mara-lake-nakuru-amboseli-safari-5318818",
    "Airport": "airport-transfers-7b08fac",
    "Kibera": "kibera-slums-tour-d986781",
    "KTanzania": "7-dayskenya-tanzania-safaris-combined-8453c29",
    "9KenyaTz": "9-days-combined-kenya-tanzania-safari-adventure-efd5b06",
    "12KenTz": "12-days-combined-kenya-tanzania-nairobi-l-nakuru-masai-mara-serengeti-ngorongoro-l-manyara-tarangire-arusha-safari-1207749"
}

service = Service('/usr/bin/chromedriver')


driver = webdriver.Chrome(service=service)
#__width-initial
details = {
    "overview" : "elementor-element elementor-element-1207749 elementor-widget elementor-widget-text-editor",
    "inclusions" : "elementor-container elementor-column-gap-default"
}


url = 'https://kairi.co.ke/12-days-combined-kenya-tanzania-nairobi-l-nakuru-masai-mara-serengeti-ngorongoro-l-manyara-tarangire-arusha-safari'

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

# Extract overview text (adjust selectors if necessary)
overviews = soup.find_all('div', class_=f'{details["overview"]}')
for overview in overviews:
    info[detail_keys[0]] = {}
    info[detail_keys[0]] = overview.get_text()
    print(overview.get_text())

# Extract inclusion text (adjust selectors if necessary)
inclusions = soup.find_all('div', class_=f'{details["inclusions"]}')
for inclusion in inclusions:
    info[detail_keys[1]] = {}
    info[detail_keys[1]] = inclusion.get_text()
    print(inclusion.get_text())

with open(f'kairi/f12.json', 'w') as json_file:
    json.dump({ 'f12': info}, json_file, indent=4)

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
with open(f'kairi/f12.json', 'r') as json_file:
    data = json.load(json_file)

# Step 2: Clean the data (remove a given space sequence)
space_sequence = "      "  # For example, removing 6 consecutive spaces
cleaned_data = clean_spaces(data, space_sequence)

# Step 3: Write the cleaned data to a new JSON file
with open(f'kairi/f12.json', 'w') as cleaned_file:
    json.dump(cleaned_data, cleaned_file, indent=4)

print("Specific space, newline and tab characters removed successfully!")