# -*- coding: utf-8 -*- 

import scrapy
from scrapy import Request
import urlparse
from urlparse import urljoin
#from urllib.parse import urljoin

class SpiderSpider(scrapy.Spider):
    name = 'new'
    allowed_domains = ['www.avvo.com/all-lawyers/ny/new_york.html']
    start_urls = ['http://www.avvo.com/all-lawyers/ny/new_york.html']

    def parse(self, response):
        links=response.css('div.row a.v-pa-list-link::attr("href")').extract()
        for link in links: 
            url=response.urljoin(link)
            yield scrapy.Request(url, callback=self.parse_new)
           
    def parse_new(self, response):  
         news=response.css('div.row a.v-serp-block-link::attr("href")').extract()
         for new in news:
            newu =response.urljoin(new)
            yield scrapy.Request(url, callback=self.parse_details)
    def parse_details(self, response):
        yield{
             'name':response.css('title::text').extract_first()
             'about':response.css('div.card p::text').extract()
             'license':response.css('li time::text').extract()
             'avvo_rating':response.css('.row span.h3::text').extract()
             'client_rating':response.css('.row span.small::text').extract()
             'image_url':response.css('.row img::attr(src)').extract_first()
              }                        
            
