import csv
from pathlib import Path
from constants import *

data_folder = Path(ROOT_DIRECTORY)
appartment = {}
with open(data_folder / APPARTMENTS_OUTPUT_FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        appartment.setdefault(row['city'], {})
        # Prepare associative array with city room capacity and prices
        appartment[row['city']].setdefault(row['capacity'], {})
        appartment[row['city']][row['capacity']].setdefault('price', 0)
        appartment[row['city']][row['capacity']].setdefault('count', 0)
        appartment[row['city']][row['capacity']]['price'] += int(row['price'])
        appartment[row['city']][row['capacity']]['count'] += 1

#Print stats for rooms
for city_name, room in appartment.items():
    for capacity, v in room.items():
        avg_price = v['price']/v['count']
        print(city_name + ": $" + str(round(avg_price,2)) + " for " + str(capacity) + " person room")
