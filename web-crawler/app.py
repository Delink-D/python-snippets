# a program that crawls the web web or info
import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    pages = 2               # set the page nuber to crawl

    while pages <= max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(pages)
        source_code = requests.get(url)

        plane_text = source_code.text

        soup = BeautifulSoup(plane_text)

        for link in soup.findAll('a', {'class': 'title'}):
            href = link.get('href')
            title = link.string

            print(href)
            print(title)

    pages += 1   # increment the page by one

spider(2)
