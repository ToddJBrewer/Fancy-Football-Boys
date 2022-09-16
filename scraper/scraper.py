import requests
from bs4 import BeautifulSoup
import re

def make_soup(url):
    # Set headers to have a user agent to prevent 403 Error
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0"}
    # Get the html from the url and store in page
    page = requests.get(url, headers=headers)
    # Create and return html soup using lxml parser
    return BeautifulSoup(page.text, "lxml")

def clean(soup):
    # Get all tags with a "row0 right" class
    rows = soup.find_all(class_="row0 right")
    return rows

def main():
    url="https://www.footballdb.com/fantasy-football/index.html?pos=QB&yr=2022&wk=1&key=48ca46aa7d721af4d58dccc0c249a1c4"
    # Store soup (undecided on type, leaning towards chicken noodle)
    soup = make_soup(url)
    clean_soup = clean(soup)
    with open("rows.html", "w") as outfile:
        outfile.write("<table>")
        outfile.write(str(clean_soup))
        outfile.write("</table>")


if __name__ == "__main__":
    main()

