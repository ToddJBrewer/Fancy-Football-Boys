import requests
from bs4 import BeautifulSoup
import re

class Scraper():
    def __init__(self):
        # Set headers to have a user agent to prevent 403 Error
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)" +
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

    # Method to get the URL and turn it into soup!
    def make_soup(self, url):
        # Get the html from the url and store in page
        page = requests.get(url, headers=self.headers)
        # Create and return html soup using lxml parser
        return BeautifulSoup(page.text, "lxml")

    # Method to get everything within an argued class
    def strain(self, soup, class_name):
        data = soup.find_all(class_=class_name)
        return data

    # Mthod to find all occurrences of an argued tag
    def find_all_tags(self, soup, tag):
        data = soup.find_all("tr")
        return data

