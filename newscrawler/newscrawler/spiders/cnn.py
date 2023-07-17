import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from newscrawler.items import Article

class CnnSpider(CrawlSpider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/"]
    rules = [Rule(LinkExtractor(allow=r'\/2023\/[0-9][0-9]\/[0-9][0-9]\/[a-zA-Z\-]+\/[a-zA-Z\-]+\/index.html'),callback="parse_info",follow=True)]

    def parse_info(self, response):
        article = Article()
        article["url"] = response.url
        article["source"] = "CNN"
        article["title"] = response.xpath("//title/text()").get()
        article["description"]=response.xpath("//meta[@name='description']/@content").get()
        article["date"]= response.xpath("//meta[@property='article:published_time']/@content").get()
        article["author"]=response.xpath("//meta[@name='author']/@content").get()
        return article
