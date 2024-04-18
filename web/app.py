from flask import Flask, render_template, request
# import scrape_wiki
# 
import sys
import os
# Temporary modification to sys.path
project_root = os.path.dirname(os.path.abspath((os.path.abspath(__file__))))  # Get the directory of app.py
sys.path.insert(0, "W:\Projects\LLMWiki-Project")  # Add it to the front of sys.path
# W:\Projects\LLMWiki-Project
print(project_root)
from src import scrape_wiki
app = Flask(__name__)


@app.route('/')
def index():
    print("POG")
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    print("Incoming scrape request!") 
    target = request.args.get('target')
    print(target)
    scrape_wiki.scrape_wiki(target) 
    return "Scraping complete!"

@app.route('/search')
def search():
    query = request.args.get('query')

    with open('scraped_text.txt', 'r', encoding="utf-8") as file:
        text = file.read()
    results = []
    # Simple substring search (case-insensitive)
    if query.lower() in text.lower():
        # Find the paragraph containing the query
        paragraphs = text.split('\n')
        for paragraph in paragraphs:
            if query.lower() in paragraph.lower():
                results.append(paragraph)
        if results : return results
        return "Relevant paragraph not found."  # Refined if nothing's found
    else:
        return "Query not found in the scraped text."

if __name__ == '__main__':
    app.run(debug=True)