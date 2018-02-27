# -*- coding: utf-8 -*-
import scrapy
from logging import warning

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    # allowed_domains = ['www.zhaopin.com']
    start_urls = ['https://passport.zhaopin.com/account/login']

    def parse(self, response):
        warning("{}".format(response.status))
        return scrapy.FormRequest.from_response(
                response,
                formdata={
                    'int_count': '999',
                    'errUrl': "https://passport.zhaopin.com/account/login",
                    'RememberMe': 'false',
                    'requestFrom': 'portal',
                    'loginname':'925370765@qq.com',
                    'Password': 'xxx',
                },
                callback=self.after_login
        )

    def after_login(self,response):
        self.logger.warn("{}".format(response.url))
        #self.logger.warn("{}".format(type(response.url)))
        if  response.url == "https://i.zhaopin.com":
             self.logger.warn("Login sucess")
        else:
            self.logger.error("Login fail")
        return