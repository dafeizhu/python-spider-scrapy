# -*- coding: utf-8 -*-
import scrapy
from hr10.items import Hr10Item
   
class HrSpiderSpider(scrapy.Spider):
    # 访问腾讯招聘网
    name = 'hr_spider'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?start=0#a']

    def parse(self, response):
        # 通过CSS选择器参数属性提取数据
        tr1 = response.css("tr[class='even']")
        tr2 = response.css("tr[class='odd']")
        trs = tr1 + tr2
        # 遍历获取到的对象
        for tr in trs:
            # 定义一个空的字典item
            item = Hr10Item()
            # 因为爬取下来的数据为被注释了的信息 所以将爬取结果去除注释符并去除空格
            job_name = tr.css("td a::text").extract()[0]
            detail_link = tr.css("td a::attr(href)").extract()[0]
            public_data = tr.css("td").extract()[4].replace('<td>','').replace('</td>','')
            location = tr.css("td").extract()[3].replace('<td>','').replace('</td>','')
            people_num = tr.css("td").extract()[2].replace('<td>','').replace('</td>','')
            job_type = tr.css("td").extract()[1].replace('<td>','').replace('</td>','')
            # 将处理完的数据一个个存储到字典中
            item["detail_link"] = "https://hr.tencent.com/" + detail_link
            item["job_name"] = job_name
            item["public_data"] = public_data
            item["location"] = location
            item["people_num"] = people_num
            item["job_type"] = job_type
            request = scrapy.Request(url = item["detail_link"],callback = self.parse_body)
            request.meta["item"] = item
            yield request
        # 利用xpath定位网页中下一页的链接
        next_page = response.xpath("//a[@id='next']/@href").extract()[0]
        # 通过遍历访问完成数据爬取
        if next_page:
            yield scrapy.Request(url = "https://hr.tencent.com/" + next_page,callback=self.parse)


    # 这个一个回调函数，结果返回到34行的request中
    def parse_body(self,response):
        # 同样的 也是利用xpath定位工作职责跟工作要求
        item = response.meta["item"]    
        job_duty = response.xpath("//tr[@class='c'][1]/td/ul/li/text()").extract()
        job_order = response.xpath("//tr[@class='c'][2]/td/ul/li/text()").extract()
        job_duty = "\n".join(job_duty)
        job_order = "\n".join(job_order)
        item["content"] = "工作职责：\n" + job_duty + "\n工作要求：\n" + job_order
        yield item


