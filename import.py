from atira.locations import LocationScraper
from atira.appartments import AppartmentScraper
from atira.appartment_info import AppartmentInfoScraper
from constants import *
import json

url = ATIRA_URL
objs_appartment = []
appartment_links = []

print('Data Scrapping in Progress...')
#Fetch all the links for the available buildings
location = LocationScraper(url)
location_links = location.get_location_links()

#Fetch all the links of the rooms available in each building
for link in location_links:
    objs_appartment.append(AppartmentScraper(link))

for apprartment in objs_appartment:
    appartment_links.append(apprartment.get_appartment_links())

#Fetch all the information of the rooms available in each building
appartments_info = []
for links in appartment_links:
    for link in links:
        appar_info = AppartmentInfoScraper(link)
        appartment = appar_info.get_appartment()
        appartments_info.append(appartment)

# Saving appartments info in csv
appar_info = AppartmentInfoScraper()
appar_info.save_all(appartments_info)

print('Scrapping done.')
# print(json.dumps(appartments_info))