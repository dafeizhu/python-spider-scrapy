from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hr10.spiders.hr_spider import HrSpiderSpider
from hr10.db import Hr10Info

# 在Scrapy框架内控制爬虫
if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())
    process.crawl("hr_spider")
    
    # 控制台主界面
    main = int(input("请输入操作类型：（1或2）"))
    if main == 1:
        process.start()

    elif main == 2:
        keyword = input("关键字：")
        city = input("城市：")
        job_type = input("职业类型：")
        begin = input("起点位置：")
        total = input("显示多少记录：")
        print(Hr10Info("hrinfo10").outinfo(keyword,city,job_type,begin,total))

    else:
        print("输入错误！")

