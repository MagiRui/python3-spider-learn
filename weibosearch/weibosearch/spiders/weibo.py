# -*- coding: utf-8 -*-
import json
import re

import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    search_url = "https://weibo.cn/search/mblog?hideSearchFrame="
    max_page = 100

    def start_requests(self):

        keyword = "000001"
        url ="{url}&keyword={keyword}".format(url=self.search_url, keyword=keyword)
        for page in range(self.max_page + 1):

            data = {

                "mp":str(self.max_page),
                "page":str(page)
            }

            yield scrapy.FormRequest(url, callback=self.parse_index, formdata=data)

    def parse_index(self, response):

        weibos = response.xpath('//div[@class="c" and contains(@id, "M_")]')
        for weibo in weibos:

            is_forward = bool(weibo.xpath('.//span[@class="cmt"]').extract_first())
            if  is_forward:

                detail_url = weibo.xpath('.//a[contains(., "原文评论[")]//@href').extract_first()
            else:

                detail_url = weibo.xpath('.//a[contains(., "评论[")]//@href').extract_first()

            yield scrapy.Request(detail_url, callback=self.parse_detail)

    def parse_detail(self, response):

        id = re.search('comment\/(.*?)\?', response.url).group(1)
        url = response.url
        content = response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract_first()

        print(id, url, content)

