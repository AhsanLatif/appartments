import requests
import bs4
import time
import numpy as np
from pathlib import Path


class AbstractScraper():

    def __init__(self, url):
        user_agent = self.get_random_ua()
        try:
            HEADERS = {
                'User-Agent': user_agent.replace('\n', ''),
            }
            self.soup = bs4.BeautifulSoup(
                requests.get(
                    url,
                    headers=HEADERS
                ).content,
                "html.parser"
            )
        except Exception as ex:
            print(str(ex))


    def get_random_ua(self):
        random_ua = ''
        data_folder = Path("appartments")
        ua_file = data_folder / 'user_agents.txt'
        try:
            with open(ua_file) as f:
                lines = f.readlines()
            if len(lines) > 0:
                prng = np.random.RandomState()
                index = prng.permutation(len(lines) - 1)
                idx = np.asarray(index, dtype=np.integer)[0]
                random_ua = lines[int(idx)]
        except Exception as ex:
            print('Exception in random_ua')
            print(str(ex))
        finally:
            return random_ua