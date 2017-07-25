import scrapy


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
        if 'Invalid login' in response.body:
            self.logger.error('Login Failed')
            return
        links = response.xpath('//div[@id="linkNav"]/ul/li')
        for link in links:
            link1 = link.xpath('./a/@href').extract_first()
            # item = siteItem()
            print('***LINK*** %s' % link1)
