import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from newscrawler.items import Article

class ApnSpider(CrawlSpider):
    name = "apn"
    allowed_domains = ["apnews.com"]
    start_urls = ["https://apnews.com/"]
    rules = [Rule(LinkExtractor(allow=r'\/article\/[a-z A-Z\-]+\-[a-zA-Z0-9]'),callback='parse_info',follow=True)]

    def parse_info(self, response):
        article = Article()
        article["url"] = response.url
        article["source"] = "Associated Press News"
        article["title"] = response.xpath("//meta[@property='og:title']/@content").get()
        article["description"]=response.xpath("//meta[@property='og:description']/@content").get()
        article["date"]= response.xpath("//meta[@property='article:published_time']/@content").get()
        article["author"]=response.xpath("//div[@class='Page-authors']/span[@class='Link']/text()").get()
        return article
