import requests
import json
from bs4 import BeautifulSoup

def check_structure(url):
    print(f"Checking page structure of {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Read exisiting JSON
    with open('results.json', 'r') as f:
        data = json.load(f)

    # Get all page elements
    all_elements = soup.find_all(True)


    for element in all_elements:
        tag_name = element.name
        print(tag_name)



    