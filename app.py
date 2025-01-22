import requests
from bs4 import BeautifulSoup

url = "https://paulbogard.net/personal-website-history/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')
for img in images:
    if not img.get('alt'):
        print(f"Image missing alt text: {img}")
    else:
        print(f"Image alt text: {img['alt']}")