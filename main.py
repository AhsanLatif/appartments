from appartments.atira.locations import LocationScraper
from appartments.atira.appartments import AppartmentScraper
from appartments.atira.appartment_info import AppartmentInfoScraper
from constants import *
import json

url = ATIRA_URL
objs_appartment = []
appartment_links = []

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
appartment = {}
for links in appartment_links:
    for link in links:
        appar_info = AppartmentInfoScraper(link)
        appartment_info = {}
        appartment_info['price'] = appar_info.get_price()
        appartment_info['capacity']  = appar_info.capacity_of_persons()
        appartment_info['room_name'] = appar_info.room_name()
        appartment_info['building_name'] = appar_info.building_name()
        appartment_info['location'] = appar_info.location()
        appartment_info['features'] = appar_info.features()
        appartment_info['city'] = appar_info.city()
        appartments_info.append(appartment_info)
        appartment.setdefault(appartment_info['city'], {})
        #Prepare associative array with city room capacity and prices
        appartment[appartment_info['city']].setdefault(appartment_info['capacity'], {})
        appartment[appartment_info['city']][appartment_info['capacity']].setdefault('price', 0)
        appartment[appartment_info['city']][appartment_info['capacity']].setdefault('count', 0)
        appartment[appartment_info['city']][appartment_info['capacity']]['price'] += int(appartment_info['price'])
        appartment[appartment_info['city']][appartment_info['capacity']]['count'] += 1

#Calculate avaerage prices per room capcacity in each city and print
for city_name, room in appartment.items():
    for capacity, v in room.items():
        avg_price = v['price']/v['count']
        print(city_name + ": $" + str(round(avg_price,2)) + " for " + str(capacity) + " person room")

# Saving appartments info in csv
appar_info = AppartmentInfoScraper()
appar_info.save_all(appartments_info)

# print(json.dumps(appartments_info))
