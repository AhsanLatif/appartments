import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}


class AbstractScraper():

    def __init__(self, url, test=False):
        self.soup = BeautifulSoup(
            requests.get(
                url,
                headers=HEADERS
            ).content,
            "html.parser"
        )
        time.sleep(3)