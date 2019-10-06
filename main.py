from appartments.atira.locations import LocationScraper
from appartments.atira.appartments import AppartmentScraper
from appartments.atira.appartment_info import AppartmentInfoScraper

url = "https://atira.com/locations/"

apar = LocationScraper(url)
location_links = apar.get_location_links()
objs_appartment = []
appartment_links = []
for link in location_links:
    objs_appartment.append(AppartmentScraper(link))

for apprartment in objs_appartment:
    appartment_links.append(apprartment.get_appartment_links())

appartments_info = []
for links in appartment_links:
    for link in links:
        appartment_info = {}
        appar_info = AppartmentInfoScraper(link)
        print(link)
        price = appar_info.get_price()
        print(price)
        capcacity = appar_info.capacity_of_persons()
        room_name = appar_info.room_name()
        building_name = appar_info.building_name()
        location = appar_info.location()
        feature = appar_info.features()
        appartment_info['price'] = price
        appartment_info['capacity'] = capcacity
        appartment_info['room_name'] = room_name
        appartment_info['building_name'] = building_name
        appartment_info['location'] = location
        appartment_info['features'] = feature
        appartments_info.append(appartment_info)
print(appartments_info)
