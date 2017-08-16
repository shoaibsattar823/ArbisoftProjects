from spider import Spider
from bs4 import BeautifulSoup


class DarazSpider(Spider):
    def parse(self, page):
        links = []
        soup = BeautifulSoup(page)
        for link in soup.find_all('a'):
            if link.get('href') is not None:
                if link.get('title'):
                    links.append([link.get('href').encode('utf-8'),
                                 link.get('title').encode('utf-8')])
                else:
                    links.append([link.get('href').encode('utf-8'),
                                 link.text.encode('utf-8')])
        return links


def main():
    spider = DarazSpider()
    html = spider.get_html('https://www.daraz.pk/catalog/?q=samsung')
    links = spider.parse(html)
    spider.save_output(links, 'links.csv')

if __name__ == '__main__':
    main()
