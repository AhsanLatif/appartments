from appartments.atira.locations import LocationScraper
from appartments.atira.locations import AppartmentScraper
from appartments.atira.appartment_info import AppartmentInfoScraper

url = "https://atira.com/locations/"
url1 = "https://atira.com/location/merivale-st/"
url2 = "https://atira.com/room/glen-rd/twin-share-3/"

# apar = LocationScraper(url)
# data_loc = apar.get_location_links()
appartment_info = {}
appar_info = AppartmentInfoScraper(url2)
price = appar_info.get_price()
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
print(appartment_info)
#
# apar = AppartmentScraper(url1)
# app_loc = apar.get_appartment_links()

# print(data_loc)

# data_appartments =
# print(app_loc)
print("Hello world!")