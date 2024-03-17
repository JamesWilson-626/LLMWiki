import requests
from bs4 import BeautifulSoup

def scrape_elden_ring_wiki():
    base_url = "https://eldenring.wiki.fextralife.com/Elden+Ring+Wiki"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all possible text-containing elements
    text_elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li', 'span']) 

    # Extract and print text from each element 
    for element in text_elements:
        text = element.get_text(strip=True)
        if text:  # Avoid printing empty strings
            print(text)
     
     
if __name__ == "__main__":      
    scrape_elden_ring_wiki()