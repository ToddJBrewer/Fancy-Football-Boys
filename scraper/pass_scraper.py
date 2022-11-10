import requests
from bs4 import BeautifulSoup
import re
import csv
from scraper import Scraper
from html_cleaner import HTML_Cleaner

def main():
    url="https://www.footballdb.com/statistics/nfl/player-stats/passing/2022/regular-season?sort=passyds"
    # Store soup (undecided on type, leaning towards chicken noodle)
    scraper = Scraper()
    soup = scraper.make_soup(url)
    clean_soup = scraper.strain(soup, "statistics scrollable")

    
    with open("../data/passing.csv", 'w') as outfile:
        pass

    cleaner = HTML_Cleaner()
    rows = cleaner.split_on_tag(soup, "tr")
    for row in rows:
        row = row[1]
        row = cleaner.replace_tag(row, "</td>", ',')
        row = cleaner.replace_tag(row, "</th>", ',')
        row = cleaner.remove(row, "<span class=\"visible-xs\">", "</span>")
        row = cleaner.remove_tag(row, 'a')
        row = cleaner.remove_tag(row, "span")
        row = cleaner.remove_tag(row, "td")
        row = cleaner.remove_tag(row, "th")
        row = row[:-1]
        row = row.split(",")

        with open("../data/passing.csv", 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(row)

if __name__ == "__main__":
    main()

