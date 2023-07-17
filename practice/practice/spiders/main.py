import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        title = response.xpath('//span[@class="title"]/text()').get()
        subtitle = response.xpath('//span[@class="subtitle"]/text()').get()
        address = response.xpath('//span[@class="address"]/text()').get()
        return{
            "title" : title,
            "subtitle" : subtitle,
            "address" : address
        }

