 # Import Statements
import requests as r
import csv
import pandas as pd
import re
from bs4 import BeautifulSoup as bs


def scraper():
    # Grabbing the URL page
    social_blade = r.get('https://socialblade.com/instagram/user/selenagomez')

    # Grabbing only the html elements of the page
    sb_html = bs(social_blade.content, 'lxml')

    results = sb_html.find_all("div", {"class": "stats-top-data-content"})
    
    stats = [];

    for i in results:
        stats.append(clean_text(i))

    print(stats)    

# Takes in genius kitchens HTML content
# Finds the real URL, cleans it up, and returns it as a string
def clean_text(data):
    data_to_ret = data.text;
    data_to_ret = data_to_ret.replace("<div class=\"stats-top-data-content\"", "")
    data_to_ret = data_to_ret.replace(" style=\"font-size: 0.9em;\">", '')
    data_to_ret = data_to_ret.replace("</div>", '')
    data_to_ret = data_to_ret.replace("\"", '')
    return data_to_ret.strip()

# Calling the scraper method
scraper()
