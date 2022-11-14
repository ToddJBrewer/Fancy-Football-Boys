import requests
from bs4 import BeautifulSoup
import re
import csv
from scraper import Scraper
from html_cleaner import HTML_Cleaner

class fdb_scraper():
    scraper = None
    cleaner = None
    
    def __init__(self):
        self.scraper = Scraper()
        self.cleaner = HTML_Cleaner()

    def wipe_file(self, file):
        with open(file, 'w') as file:
            pass

    def scrape(self, url, output_file):
        # Store soup (undecided on type, leaning towards chicken noodle)
        soup = self.scraper.make_soup(url)
        clean_soup = self.scraper.strain(soup, "statistics scrollable")

        self.wipe_file(output_file)

        rows = self.cleaner.split_on_tag(soup, "tr")
        with open(output_file, 'a') as outfile:
            writer = csv.writer(outfile)
            for row in rows:
                row = row[1]
                row = self.cleaner.replace_tag(row, "</td>", '\t')
                row = self.cleaner.replace_tag(row, "</th>", '\t')
                row = self.cleaner.remove(row, "<span class=\"visible-xs\">", "</span>")
                row = self.cleaner.remove(row, "<span class=\"visible-xs-inline\">", "</span>")
                row = self.cleaner.remove_tag(row, 'a')
                row = self.cleaner.remove_tag(row, "span")
                row = self.cleaner.remove_tag(row, "td")
                row = self.cleaner.remove_tag(row, "th")
                row = row[:-1]

                writer.writerow(row.split(","))
