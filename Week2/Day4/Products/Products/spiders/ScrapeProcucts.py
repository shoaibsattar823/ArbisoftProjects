import scrapy


class ProductItem(scrapy.Item):
    image = scrapy.Field()
    brand = scrapy.Field()
    title = scrapy.Field()
    price_PKR = scrapy.Field()
    # detailpage = scrapy.Field()
    det_title = scrapy.Field()
    det_features = scrapy.Field()


class ProductSpider(scrapy.Spider):
    name = "products"
    nextp = 0

    def start_requests(self):
        url = 'https://www.daraz.pk/catalog/'
        brand = getattr(self, 'brand', None)
        if brand is not None:
            url = 'https://www.daraz.pk/catalog/?q={brand}'.format(brand=brand)
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for prod in response.css('section.products div.sku'):
            detailpage = prod.xpath('./a/@href').extract_first()
            image = prod.css('div.image-wrapper img'
                             '::attr(data-src)').extract_first()
            brand = prod.css('h2.title span.brand::text').extract_first()
            title = prod.css('h2.title span.name::text').extract_first()
            price_PKR = prod.css('span.price span'
                                 '::attr(data-price)').extract_first()
            item = ProductItem()
            item['image'] = image
            item['brand'] = brand
            item['title'] = title
            item['price_PKR'] = price_PKR
            if detailpage:
                yield scrapy.Request(detailpage,
                                     self.parse_detail, meta={'item': item})
            else:
                return

        nextpage = response.css('section.pagination [title=Next]'
                                '::attr(href)').extract_first()

        self.nextp = self.nextp + 1

        if (self.nextp != 3):
            yield response.follow(nextpage, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        item['det_title'] = response.xpath('//div[@class="details-wrapper"]'
                                           '//h1/text()').extract_first()
        item['det_features'] = response.xpath('//div[@class="detail-features"]'
                                              '//li/text()').extract()
        return item
