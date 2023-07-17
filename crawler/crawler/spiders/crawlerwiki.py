import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

class CrawlerwikiSpider(CrawlSpider):
    name = "crawlerwiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Domain_name"]

    rules = [Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'),callback="parse_info",follow=True)]

    def parse_info(self, response):
        title = response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()').get()
        url = response.url
        lastedited = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return {
            "title" : title,
            "url" : url,
            "lastedited" : lastedited
        }