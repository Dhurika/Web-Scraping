import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from recorddata.items import Article

class RecorderSpider(CrawlSpider):
    name = "recorder"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Glassdoor"]

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'),callback="parse_info",follow=True)]

    def parse_info(self, response):
        article = Article()
        article['title'] = response.xpath('//title/text()').get() or response.xpath('//title/i/text()').get()
        article['url'] = response.url
        article['lastmod'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article