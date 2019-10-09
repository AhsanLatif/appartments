from ._abstract import AbstractScraper


class AppartmentScraper(AbstractScraper):
    def get_appartment_links(self):
        links = []
        link_html = self.soup.find_all('div', attrs={'class': 'card__room'})
        for a in link_html:
            links.append(a.a['href'])
        return links
