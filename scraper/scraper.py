 # Import Statements
import requests as r
import csv
import pandas as pd
import re
from bs4 import BeautifulSoup as bs


def scraper():
    # Grabbing the URL page
    genius_kitchen = r.get(i)

    # Grabbing only the html elements of the page
    gk_html = bs(genius_kitchen.content, 'lxml')

    # Grabbing Real URL and cleaning it
    real_url = get_real_url(gk_html)

    # Grabbing Name of Dish
    dish_name = gk_html.find('h1').text.strip(' "\'\t\r\n')

    # Stripping html tags and adding ingredients to the list
    list_of_ingredients = get_ingredients_list(gk_html.find_all('span', class_= 'food'))
                    


# Returns a list of ingredients in the recipe with the html tags stripped
# Takes in the ingredients with html tags
def get_ingredients_list(ingredients):
    list_of_ingredients = []
    for i in ingredients:
        list_of_ingredients.append((i.text.strip('\n')).lower())
    return list_of_ingredients

# Takes in genius kitchens HTML content
# Finds the real URL, cleans it up, and returns it as a string
def get_real_url(gk_html):
    real_url = str(gk_html.find("meta",  property="og:url"))
    real_url = real_url.replace("<meta content=", "")
    real_url = real_url.replace("property=\"og:url\"/>", '')
    real_url = real_url.replace("\"", '')
    return real_url.strip()

# Calling the scraper method
scraper()