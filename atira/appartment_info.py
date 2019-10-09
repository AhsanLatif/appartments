from ._abstract import AbstractScraper
import re


class AppartmentInfoScraper(AbstractScraper):
    fieldnames = ["city", "building_name", "capacity", "price", "room_name", "features", "location"]

    def get_price(self):
        price = self.soup.find("span", class_="room__sidebar--rate-base").string
        return price.strip()

    def capacity_of_persons(self):
        capacity = self.soup.find("div", class_="room__sidebar--icons").ul.li.strings
        for cap in capacity:
            if cap is not None:
                return cap.strip()

    def features(self):
        feature_all = []
        feature_html = self.soup.find_all("div", class_="room__feature--description wysiwyg")
        for feature in feature_html:
            feature_all.append(feature.p.get_text())
        return feature_all

    def room_name(self):
        title = self.soup.find("h1", class_="room__title").string
        return title.strip()

    def building_name(self):
        building = self.soup.find("h5", class_="room__location--title").string
        return building.strip()

    def location(self):
        add_html = self.soup.find("div", class_="address").span
        add1 = add_html.string
        add2 = add_html.next_sibling.next_sibling.string
        address = add1 + add2
        return address.strip()

    def city(self):
        html_city = self.soup.select('div[class*="location-city-"]')
        x = re.search("(location-city-)(.*?)[\s]", str(html_city[0]))
        return x.group(0)[14:].strip()

    def save_all(self, data, format='csv'):
        super().save_all(data, format)
