# -*- coding: utf-8 -*-
import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['http://www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['http://http://www.avvo.com/all-lawyers/ny/new_york.html/']

    def parse(self, response):
       for spider in response.css('div.spider'):
            yield {
                'name': spider.css('title::text').extract_first(),
                'about': spider.css('.card p::text').extract(),
                'license': spider.css('li time:text').extract_first(),
                'avvo_ratting':spider.css('.h3::text').extract_first()'
                'image_url':response.css('img').xpath('@src').extract_first()
            }
