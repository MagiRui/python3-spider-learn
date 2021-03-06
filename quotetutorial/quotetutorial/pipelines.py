# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

from scrapy.exceptions import DropItem


class TextPipeLine(object):

    def __init__(self):

        self.limit = 30

    def process_item(self, item, spider):


        if item["text"]:

            if len(item["text"]) > self.limit:

                item["text"] = item["text"][0:self.limit].rstrip() + "..."
            return item
        else:

            return DropItem("Missing Text")

class MongoPipeline(object):

    def __init__(self, mongo_url, mongo_db):

        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):

        return cls(

            mongo_url=crawler.settings.get("MONGO_URL"),
            mongo_db=crawler.settings.get("MONGO_DB")
        )

    def open_spider(self, spider):

        self.client  = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):

        print(item)
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):

        self.client.close()