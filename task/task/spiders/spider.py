# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['http://www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['http://http://www.avvo.com/all-lawyers/ny/new_york.html/']

    def parse(self, response):
       for spider in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
