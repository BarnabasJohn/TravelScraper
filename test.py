'''
from park import AberdareCompanies
import json

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

company_dict = {}

for index, (key, value) in enumerate(company.items()):
    print(f"Index {index}: Key = {key}, url = {value['url']}, element = {value['element']}, class = {value['class']}")

    company_dict[key] = {}
    company_dict[key]['url'] = value['url']
    company_dict[key]['element'] = value['element']
    company_dict[key]['class'] = value['class']


print(company_dict)

with open('Aberdare/data.json', 'w') as json_file:
        json.dump({"Company": company_dict}, json_file, indent=4)


#Company json
data = [
    {"name": "John"},
    {"city": "New York"}
]
# Writing JSON data to a file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print('data written to data.json')

#json.dump({"books": books_data}, json_file, indent=4)



AberdareCompanies = {
    "AfricanTrailsExped" : "t68823",
    "SpiritofKenya" : "t18403",
    "KamerazofAfrica" : "t42514",
    "ApodiformesAdventures" : "t71350",
    "LionRiderTours" : "t70838",
    "TravInteractive" : "t59284",
    "KibokoTours":"t58253"
}

for (mkey, mvalue) in AberdareCompanies.items():
      print(f"key = {mkey} and value = {mvalue}")

for (mkey, mvalue) in AberdareCompanies.items():
    def clean_spaces(data, space_sequence):
        if isinstance(data, dict):
            return {key: clean_spaces(value, space_sequence) for key, value in data.items()}
        elif isinstance(data, list):
            return [clean_spaces(item, space_sequence) for item in data]
        elif isinstance(data, str):
            # Remove the given sequence of spaces from strings
            return data.replace(space_sequence, ' ').replace('\n', ' ').replace('\t', ' ').replace('\u2013', '').replace('\u00a0', '')
        else:
            return data

    # Step 1: Read the JSON file
    with open(f'Aberdare/{mkey}.json', 'r') as json_file:
        data = json.load(json_file)

    # Step 2: Clean the data (remove a given space sequence)
    space_sequence = "      "  # For example, removing 6 consecutive spaces
    cleaned_data = clean_spaces(data, space_sequence)

    # Step 3: Write the cleaned data to a new JSON file
    with open(f'Aberdare/{mkey}.json', 'w') as cleaned_file:
        json.dump(cleaned_data, cleaned_file, indent=4)

print("Specific space, newline and tab characters removed successfully!")


details = {
    "overview" : "elementor-section elementor-top-section elementor-element elementor-element-735ab33 elementor-section-stretched elementor-section-boxed elementor-section-height-default elementor-section-height-default",
    "inclusions" : "elementor-section elementor-top-section elementor-element elementor-element-f985f11 elementor-section-boxed elementor-section-height-default elementor-section-height-default"
}
detail_keys = list(details.keys())
tours = {}

tours[detail_keys[0]] = {}

print(tours)
'''



