# a program that crawls the web web or info
import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    pages = 1               # set the page nuber to crawl

    while pages <= max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(pages)
        source_code = requests.get(url)

spider(1)
