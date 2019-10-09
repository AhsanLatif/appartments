from ._abstract import AbstractScraper


class LocationScraper(AbstractScraper):
    def get_location_links(self):
        links = []
        link_html = self.soup.find_all('a', attrs={'class': 'location card'})
        for a in link_html:
            links.append(a['href'])
        return links
