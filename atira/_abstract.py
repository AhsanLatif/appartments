import requests
import bs4
import numpy as np
from constants import *
import csv


class AbstractScraper():

    def __init__(self, url=None):
        if url is not None:
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
        ua_file = USERAGENT_FILENAME
        try:
            with open(ua_file) as f:
                lines = f.readlines()
            if len(lines) > 0:
                prng = np.random.RandomState()
                index = prng.permutation(len(lines) - 1)
                idx = np.asarray(index, dtype=np.integer)[0]
                random_ua = lines[int(idx)]
        except Exception as ex:
            print(EXCEPTION_RANDOM_GENERATE)
            print(str(ex))
        finally:
            return random_ua

    def save_all(self, data, format='csv'):
        if (format == 'csv'):
            with open(APPARTMENTS_OUTPUT_FILE, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()
                # Write CSV Header
                for f in data:
                    writer.writerow(f)
