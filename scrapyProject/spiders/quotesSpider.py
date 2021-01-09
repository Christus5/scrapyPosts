import scrapy


class QuotesSpider(scrapy.Spider):
    name: 'str' = 'quotes' 
    allowed_domain = ['http://quotes.toscrape.com/']
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    
    def parse(self, response, **kwargs):
        for quote in response.css('div.quote'):
            yield {
                'title': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
        for href in response.css('ul.pager a'):
            yield response.follow(href, callback=self.parse)
