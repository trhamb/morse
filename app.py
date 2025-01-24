import json
from checkers.image_checker import check_images
from checkers.heading_checker import check_headings

def initialise_results():
    initial_structure = {
        "images": [],
        "text": [],
        "headings": {
            "h1":{
                "elements": [],
                "issues": []
            },
            "h2":{
                "elements": [],
                "issues": []
            },
            "h3":{
                "elements": [],
                "issues": []
            },
            "h4":{
                "elements": [],
                "issues": []
            },
            "h5":{
                "elements": [],
                "issues": []
            },
            "h6":{
                "elements": [],
                "issues": []
            },
            
        },
        "links": [],
        "colours": []
    }
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(initial_structure, f, indent=4)

def run_checks(url):
    # Reset results file first
    initialise_results()
    
    # Run all checkers
    check_headings(url)
    check_images(url)

if __name__ == "__main__":
    url = "https://www.shorehamfort.co.uk/"
    run_checks(url)

