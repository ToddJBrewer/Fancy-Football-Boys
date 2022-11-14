import requests
from bs4 import BeautifulSoup
import re
import csv
from scraper import Scraper
from html_cleaner import HTML_Cleaner
from football_db_scraper import fdb_scraper

def main():
    scraper = fdb_scraper()
    scraper.scrape("https://www.footballdb.com/statistics/nfl/player-stats/receiving/2022/regular-season?sort=recnum", "../data/receiving.tsv")
    print("ding your receiving soup is done")

if __name__ == "__main__":
    main()