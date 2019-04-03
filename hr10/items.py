# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Hr10Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义变量
    job_name = scrapy.Field()
    detail_link = scrapy.Field()
    public_data = scrapy.Field()
    location = scrapy.Field()
    people_num = scrapy.Field()
    job_type = scrapy.Field()
    content = scrapy.Field()
    
