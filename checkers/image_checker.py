import requests
import json
from bs4 import BeautifulSoup

def check_images(url):
    # Alt text checking
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = {
        "images": [
            
        ]
    }

    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            print(f"Image missing alt text: {img}")
        else:
            print(f"Image alt text: {img['alt']}")

