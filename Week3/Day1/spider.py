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
