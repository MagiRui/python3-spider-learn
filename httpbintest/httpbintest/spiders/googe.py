# -*- coding: utf-8 -*-
import scrapy


class GoogeSpider(scrapy.Spider):
    name = 'googe'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/']

    def make_requests_from_url(self, url):

        return  scrapy.Request(url = url, meta={'download_timeout':10}, callback=self.parse,
                               dont_filter=False)

    def parse(self, response):

        print(response.text)

