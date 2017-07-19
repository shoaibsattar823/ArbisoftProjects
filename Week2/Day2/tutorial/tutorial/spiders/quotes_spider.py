import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for q in response.css('div.quote'):
            text = q.css('span.text::text').extract_first()
            author = q.css('span small.author::text').extract_first()
            tags = q.css('div.tags a.tag::text').extract()
            print dict(text=text, author=author, tags=tags)
