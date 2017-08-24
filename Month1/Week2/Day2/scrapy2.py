import scrapy


class ScrapeQuote(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/tag/inspirational/',]

    def parse1(self, response):
        for quote in response.css('div.quote'):
            yield {
                'mytext': quote.css('span.text::text').extract_first(),
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        nextpage = response.css('li.next a::attr("href")').extract_first()
        if nextpage is not None:
            yield response.follow(nextpage, self.parse1)
