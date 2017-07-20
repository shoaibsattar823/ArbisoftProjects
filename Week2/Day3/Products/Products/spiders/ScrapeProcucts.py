import scrapy


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
            yield {
                'image': prod.css('div.image-wrapper img'
                                  '::attr(data-src)').extract_first(),
                'brand': prod.css('h2.title span.brand::text').extract_first(),
                'title': prod.css('h2.title span.name::text').extract_first(),
                'price(PKR)': prod.css('span.price span'
                                       '::attr(data-price)').extract_first(),
            }

        nextpage = response.css('section.pagination [title=Next]'
                                '::attr(href)').extract_first()
        self.nextp = self.nextp + 1
        if (self.nextp != 3):
            yield response.follow(nextpage, callback=self.parse)
