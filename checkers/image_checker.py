import requests
import json
from bs4 import BeautifulSoup

def check_images(url):
    print(f"Checking images from {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Read existing JSON
    with open('results.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Get all images
    images = soup.find_all('img')
    for img in images:
        # Get neccessary details
        image_data = {
            "src": img.get('src'),
            "alt": img.get('alt'),
            "has_alt": bool(img.get('alt'))
        }
        data["images"].append(image_data)

    print("Image check complete ✅")
    
    # Write updated data back to JSON
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
