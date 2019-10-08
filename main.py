from appartments.atira.locations import LocationScraper
from appartments.atira.appartments import AppartmentScraper
from appartments.atira.appartment_info import AppartmentInfoScraper
from constants import *
import json


url = ATIRA_URL
objs_appartment = []
appartment_links = []

location = LocationScraper(url)
location_links = location.get_location_links()

for link in location_links:
    objs_appartment.append(AppartmentScraper(link))

for apprartment in objs_appartment:
    appartment_links.append(apprartment.get_appartment_links())

appartments_info = []
for links in appartment_links:
    for link in links:
        appartment_info = {}
        appar_info = AppartmentInfoScraper(link)
        appartment_info['price'] = appar_info.get_price()
        appartment_info['capacity']  = appar_info.capacity_of_persons()
        appartment_info['room_name'] = appar_info.room_name()
        appartment_info['building_name'] = appar_info.building_name()
        appartment_info['location'] = appar_info.location()
        appartment_info['features'] = appar_info.features()
        appartments_info.append(appartment_info)
        print(appartments_info)
print(json.dumps(appartments_info))

# def average_prive_room(self, appartments):
#     for appartment in appartments:

