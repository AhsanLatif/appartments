from ._abstract import AbstractScraper
from .appartments import AppartmentScraper


class LocationScraper(AbstractScraper):
    def get_location_links(self):
        links = []
        link_html = self.soup.find_all('a', attrs={'class': 'location card'})
        for a in link_html:
            links.append(a['href'])
        print(links)
        return self.get_appartment_links(links)

    def get_appartment_links(self, loc_links):
        objs_appartment = []
        appartment_links = []
        for link in loc_links:
            objs_appartment.append(AppartmentScraper(link))
        for apprartment in objs_appartment:
            appartment_links.append(apprartment.get_appartment_links())
        return appartment_links