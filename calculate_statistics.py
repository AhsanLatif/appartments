import csv
from pathlib import Path
from constants import *
from matplotlib import pyplot as plt


data_folder = Path(ROOT_DIRECTORY)
appartment = {}
with open(APPARTMENTS_OUTPUT_FILE, newline='') as csvfile:
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
    avg = []
    room_size = []
    sorted(room.keys())
    for capacity, v in sorted(room.items()):
        avg_price = v['price']/v['count']
        avg.append(avg_price)
        room_size.append(capacity)
        print(city_name + ": $" + str(round(avg_price,2)) + " for " + str(capacity) + " person room")
#Create graphs
    plt.bar(room_size, avg)
    plt.title(city_name)
    plt.ylabel('Average Price')
    plt.xlabel('Room Capacity')
    plt.savefig(OUTPUT_DIRECTORY + '/' + city_name +'.png')