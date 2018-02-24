# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#class SpidersPipeline(object):
 #   def process_item(self, item, spider):
 #       return item

class JsonWritePipeline(object):

    def open_spider(self,spider):
        self.file = open('item.jl','w')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self,item,spider):
        line = item['title']+item['href']+'\n'
        self.file.write(line)
        return item

#将爬虫的结果写进数据库
class MongonPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls,crawler):
        def from_crawler(cls,crawler):
            return cls(
                mongo_uri=crawler.settings.get('MONGO_URI'),
                mongo_db=crawler.setting.get('MONGO_DATABASE','items')
            )

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]

    def close_spider(self,spider):
        self.client.close()

    def process_item(self,item,spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item