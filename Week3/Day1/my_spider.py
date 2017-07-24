from bs4 import BeautifulSoup

import requests


class Spider:

    def get_html(self, url):
        response = requests.get(url)
        html_page = response.text
        # print('This is the requested page:\n{}').format(html_page)
        return html_page

    def save_output(self, result, outfile):
        f = open(outfile, 'w')
        for r in result:
            f.write(str(r)+'\n')
        f.close()

    def parse(self):
        pass


class DarazSpider(Spider):
    def parse(self, page):
        links = []
        soup = BeautifulSoup(page)
        for link in soup.find_all('a'):
            if link.get('href') is not None:
                links.append(link.get('href'))
        return links


def main():
    spider = DarazSpider()
    html = spider.get_html('https://www.daraz.pk/catalog/?q=samsung')
    links = spider.parse(html)
    spider.save_output(links, 'links.txt')

if __name__ == '__main__':
    main()
