# -*- coding: utf-8 -*-
import scrapy
import json
from spiders.items import *

class NovelHouweidongSpider(scrapy.Spider):
    name = 'novel_houweidong'
    allowed_domains = ['www.libaiwu.com']
    start_urls = ['http://www.libaiwu.com/hwd/']

    def parse(self, response):
        for sel in response.xpath('/html/body/div[1]/div[3]/div[3]/ul/li'):
            yield NovelItem(title=sel.xpath('a/text()').extract()[0],href=sel.xpath('a/@href').extract()[0])

