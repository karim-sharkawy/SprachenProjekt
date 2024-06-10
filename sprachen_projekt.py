import requests
from lxml import html
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
import json

# Gets the name of every language and their links
def parse_languages(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # XPath to find all <p> tags with class containing `lang--` and extract the text within the nested <a> tags
    languages = tree.xpath('//p[contains(@class, "lang--")]/a/text()')
    languages = [lang.strip() for lang in languages if lang.strip()]

    # XPath to find the link for each language
    language_links = tree.xpath('//p[contains(@class, "lang--")]/a/@href')
    base_url = "https://www.ethnologue.com"  # Base URL of the website
    full_language_links = [urljoin(base_url, link) for link in language_links]

    return languages, full_language_links

# Ensures every page is parsed so no language is missed
def find_links_to_other_pages(url):
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # XPath to find all <button> elements for different alphabet letters
    links = tree.xpath('//button[@class="tab__link"]/@onclick')
    # Extract the URL part from the onclick attribute
    links = [link.split('"')[1] for link in links if 'browse' in link]
    # Convert to full URLs
    full_links = [urljoin(url, f'/browse/names/{link}') for link in links]

    return full_links

def main(start_url):
    visited = set()
    to_visit = [start_url]
    all_languages = []
    all_full_language_links = []  # Store all full language links

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue

        visited.add(current_url)
        languages, full_language_links = parse_languages(current_url)
        all_languages.extend(languages)
        all_full_language_links.extend(full_language_links)  # Store full language links

        links = find_links_to_other_pages(current_url)
        to_visit.extend(links)

    return all_languages, all_full_language_links

start_url = 'https://www.ethnologue.com/browse/names/'
languages, full_language_links = main(start_url)

language_names = languages
language_urls = full_language_links

# Function to scrape information from individual language pages
def scrape_language_info(language_url):
    try:
        # Send a GET request to the language page
        response = requests.get(language_url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {}

        # Extract language name
        title_home = soup.find('h1', class_='title__home')
        if title_home:
            data['name'] = title_home.text.strip()

        # Extract ISO 639 code
        iso_code_element = soup.find('a', class_='chip chip--big')
        if iso_code_element:
            data['iso_code'] = iso_code_element.text.strip()

        # Extracting coordinates
        coords_tag = soup.find('div', class_='field--name-coordinates')
        if coords_tag:
            data['coordinates'] = coords_tag.text.strip().replace('Location: ', '')

        # Extract population info
        population_element = soup.find('li', class_='population__sizes')
        if population_element:
            population_div = population_element.find('div', class_='graph__langpop')
            if population_div:
                data['population'] = population_div.text.strip()

        # Extract language status (vitality)
        vitality_element = soup.find('li', class_='population__vitality')
        data['language_status'] = 'Unknown'  # Default value
        if vitality_element:
            vitality_status = vitality_element.find_all('li', class_='histogram__datum')
            for status in vitality_status:
                if 'data-count' in status.attrs and status['data-count'].isdigit() and int(status['data-count']) > 0:
                    label = status.find('label')
                    if label:
                        data['language_status'] = label.text.strip()
                        break

        return data

    except requests.RequestException as e:
        print(f"Request failed for URL {language_url}: {e}")
        return {}

# Introduce a delay of 3 seconds between each request
delay_between_requests = 3

# Combine language names and URLs into pairs
language_info_pairs = zip(language_names, language_urls)

# Dictionary to store language information
language_info_dict = {}

# Iterate over each language URL and scrape information
for language_name, language_url in language_info_pairs:
    language_info = scrape_language_info(language_url)
    language_info_dict[language_name] = language_info
    time.sleep(delay_between_requests)

# Turning into JSON file for javascript to read

# Convert the dictionary to JSON
json_data = json.dumps(language_info_dict, indent=4)

# Specify the file name
file_name = "language_info.json"

# Write JSON data to a file
with open(file_name, "w") as json_file:
    json_file.write(json_data)

# Print the name of the created file
print(f"JSON data has been saved to '{file_name}'.")
