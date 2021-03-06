import scrapy
from scrapy.http.cookies import CookieJar


class siteItem(scrapy.Item):
    title = scrapy.Field()


class LoginSpider(scrapy.Spider):
    name = "login"
    start_urls = ['https://lms.lums.edu.pk/portal']

    def parse(self, response):
        # print response.body
        user = getattr(self, 'user', None)
        pas = getattr(self, 'pas', None)
        return scrapy.FormRequest.from_response(
            response,
            formdata={'eid': user, 'pw': pas},
            callback=self.afterLogin
        )

    def afterLogin(self, response):
        # print response.body
        # print response.headers
        cookie = response.headers.getlist(
                                          'Set-Cookie'
                                          )[0].split(";")[0].split("=")
        print('*****Cookie*****', cookie)
        if 'Invalid login' in response.body:
            self.logger.error('Login Failed')
            return
        links = response.xpath('//div[@id="linkNav"]/ul/li')
        cookie = response.headers
        print cookie
        for link in links:
            link1 = link.xpath('./a/@href').extract_first()
            print('***LINK*** %s' % link1)
            cookieJar = response.meta.setdefault('cookie_jar', CookieJar())
            cookieJar.extract_cookies(response, response.request)
            # print 'cookies here: ', response.meta['cookie_jar']
            item = siteItem()
            if link1 != '#' and link1 != 'javascript:;':
                yield scrapy.Request(link1, self.parse_inside,
                                     meta={'dont_merge_cookies': True,
                                           'item': item,
                                           'cookie_jar': cookieJar}
                                         )

    def parse_inside(self, response):
        print 'Here Check: '
        rp = response.text
        # print('Response over here: ', response.text)
        item = response.meta['item']
        item['title'] = response.xpath('//div[@id="content"]'
                                       '/div/div/div/div/div'
                                       '/h2'
                                       )
        return item
