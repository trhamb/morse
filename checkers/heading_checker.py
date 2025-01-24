import requests
import json
from bs4 import BeautifulSoup

def check_headings(url):
    print(f"Starting heading checks")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Open existing JSON results file
    with open('results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # H1 Checks
    heading_one = soup.find_all('h1')

    for h in heading_one:
        h_text = h.get_text()
        data['headings']['h1']['elements'].append(h_text)

    if len(heading_one) > 1:
        data['headings']['h1']['issues'].append("Multiple H1 Elements Found")

    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print("Heading checks complete ✅")