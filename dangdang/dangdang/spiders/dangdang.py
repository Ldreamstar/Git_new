# coding:utf-8
# 爬虫文件：
# 三个参数：name allowed_domains start_urls（设置起始url，只需要设置，通常会被自动创建成请求发送）
# 一个方法：parse（解析方法，通常用于起始url对应的解析）
# 完成爬虫： 修改起始url 检查修改允许的域名 在parse方法中实现爬取逻辑
import scrapy
import requests
from ..items import DangdangItem


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]  # 过滤操作
    start_urls = ["http://search.dangdang.com/?key=python"]  # 起始url 需要自己修改

    def parse(self, response):  # 解析响应 ：response是start_url的响应
        # 定义对于网站的相关操作
        books = response.xpath('//ul[@class="bigimg"]/li')

        for book in books:
            item = DangdangItem()  # 生成一个Item对象用于存储提取到的信息
            item['name'] = book.xpath('./a[@class="pic"]/@title').extract_first()
            item['author'] = book.xpath('./p/span[1]/a[1]/@title').extract() if len(
                book.xpath('./p/span[1]/a[1]/@title')) > 0 else '无作者信息'
            item['introduction'] = book.xpath('./p[@class="detail"]/text()').extract() if len(
                book.xpath('./p[@class="detail"]/text()')) > 0 else '无简介信息'

            # 将提取到的数据提交给piplines保存输出
            yield item

        pageNum = 2
        for page in range(2, pageNum):
            page = 'http://search.dangdang.com/?key=python&page_index={}'.format(page)

            yield scrapy.Request(page, callback=self.parse)
