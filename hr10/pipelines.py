# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import json
from hr10.db import Hr10Info

# 通过管道将数据压进数据库
class Hr10Pipeline(object):
    def __init__(self):
        # self.file = open("hr10.json","w",encoding="utf-8")
        pass

    def process_item(self, item, spider):
        if item["job_name"]:
            # line = json.dumps(dict(item))+"\n"
            # self.file.write(line.encode("utf-8").decode("unicode_escape"))
            hr10 = Hr10Info("hrinfo10")
            hr10.add_hr10(item["job_name"],item["detail_link"],item["public_data"],item["location"],item["people_num"],item["job_type"],item["content"])
            return item
        else:
            raise DropItem("没有标题 %s"%item)
