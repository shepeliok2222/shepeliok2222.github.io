import requests
from bs4 import BeautifulSoup
import os

def fetch_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.get_text()

def combine_texts(text1, text2):
    return text1 + "#\n" + text2

def main():
    url1 = os.getenv('APP_ADS_URL1')
    url2 = os.getenv('APP_ADS_URL2')
    
    if not url1 or not url2:
        print("URLs are not set properly.")
        return
    
    text1 = fetch_text(url1)
    text2 = fetch_text(url2)
    combined_text = combine_texts(text1, text2)

    output_file = "app-ads.txt"
    if os.path.exists(output_file):
        with open(output_file, 'r') as file:
            existing_text = file.read()
    else:
        existing_text = ""

    changes_detected = "false"
    if combined_text != existing_text:
        with open(output_file, 'w') as file:
            file.write(combined_text)
        changes_detected = "true"

    # Write the result to an environment file
    print(f"::set-output name=changes_detected::{changes_detected}")

if __name__ == "__main__":
    main()
