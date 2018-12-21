# -*- coding: utf-8 -*- 
import scrapy

class NewSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['http://www.avvo.com/all-lawyers/ny/new_york.html']

    def parse(self, response):
        for first in response.css('div.row a.v-pa-list-link::attr("href")').extract():
            yield scrapy.Request(response.urljoin("/"+first), callback=self.parse_first)
    def parse_first(self, response):
        for url in response.css('div.row a.v-serp-block-link::attr("href")').extract():
            yield scrapy.Request(response.urljoin(+url), callback=self.parse_second)
    def parse_second(self,response):
        yield {
             'name':response.css('div.row span.name::text').extract_first()
              }
