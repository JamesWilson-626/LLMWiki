import requests
from bs4 import BeautifulSoup
import sys  # For command-line arguments


def scrape_wiki(url):
    base_url = "https://eldenring.wiki.fextralife.com/Elden+Ring+Wiki"
    base_url = url
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all possible text-containing elements
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'span']) 

    # Extract and print text from each element 
    for element in text_elements:
        text = element.get_text(strip=True)
        if text:
            print(text)
            
            
    with open("scraped_text.txt", "w", encoding="utf-8") as f:
        for element in text_elements:
            text = element.get_text(strip=True)
            f.write(text + "\n")  # Add newline for paragraphs 
     
     
if __name__ == "__main__":      
    if len(sys.argv) > 1:
        url = sys.argv[1] 
        scrape_wiki(url)
    else:
        print("Please provide a wiki page URL.")